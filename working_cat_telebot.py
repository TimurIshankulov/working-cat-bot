import datetime
import time
import shelve
import logging
import traceback

from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telebot import apihelper, util, types
from models import User
from config import log_file, shelve_users
import texts

logger = logging.getLogger('TeleBot')

fill='█'
zfill='░'
fill_len = 15

class WorkingCatTeleBot(TeleBot):

    def __init__(self, token, threaded=True, skip_pending=False, num_threads=2):
        TeleBot.__init__(self, token=token, threaded=threaded,
                         skip_pending=skip_pending, num_threads=num_threads)
        self.timers = []

    def log(self, log_event):
        """Logs event to file, console and sends log message to <admin_list>"""
        log_event = '[{0}] {1}'.format(datetime.now().strftime("%d.%m.%Y %H:%M:%S"), log_event)
        with open(log_file, 'a+') as f:
            f.write(log_event + '\n')
        print(log_event)
        if self.admin_list:
            for admin in self.admin_list:
                self.send_message(admin, log_event)

    def get_user(self, user_id):
        """Returns user if found else empty class instance"""
        user_id = str(user_id)
        with shelve.open(shelve_users) as users:
            try:
                user = users[user_id]
                return user
            except KeyError:
                pass
        return User()

    def get_keyboard(self, status):
        """Returns keyboard depending on <status>"""
        keyboard = ReplyKeyboardMarkup(True, True)
        if status == 'idle':
            keyboard.row('Статус', 'Работа')

        elif status == 'choose_work':
            keyboard = InlineKeyboardMarkup()
            inline_wash_dish = InlineKeyboardButton(text='Мыть посуду (10 мин., 5 ед. опыта)', callback_data='wash_dish')
            keyboard.add(inline_wash_dish)
            inline_vacuum = InlineKeyboardButton(text='Пропылесосить (20 мин., 7 ед. опыта)', callback_data='vacuum')
            keyboard.add(inline_vacuum)
            inline_bake = InlineKeyboardButton(text='Выпекать шарлотку (30 мин., 10 ед. опыта)', callback_data='bake')
            keyboard.add(inline_bake)
            inline_back = InlineKeyboardButton(text='Назад', callback_data='back_from_choosing_work')
            keyboard.add(inline_back)

        elif status == 'on_work':
            keyboard.row('Статус', 'Работа')
        
        return keyboard

    def add_timer(self, user, chat_id, start_timestamp, seconds):
        timer = {'user': user, 'chat_id': chat_id,
                 'start_timestamp': start_timestamp, 'seconds': seconds}
        self.timers.append(timer)
    
    def handle_timers(self):
        """Handles active timers, sends it to members"""
        current_timestamp = int(time.time())
        for timer in self.timers[::1]:
            if current_timestamp - timer['start_timestamp'] >= timer['seconds']:
                user = timer['user']
                if user.status == 'on_work':
                    user.status = 'idle'
                    user.save()
                    reply = texts.WORK_DONE.format(user.cat_name)
                    keyboard = self.get_keyboard(user.status)
                    self.send_message(timer['chat_id'], reply, reply_markup=keyboard)
                self.timers.remove(timer)
    
    
    def _TeleBot__threaded_polling(self, non_stop = False, interval = 0, timeout = None, long_polling_timeout = None,
                           logger_level=logging.ERROR, allowed_updates=None):
        if not(logger_level) or (logger_level < logging.INFO):
            warning = "\n  Warning: this message appearance will be changed. Set logger_level=logging.INFO to continue seeing it."
        else:
            warning = ""
        logger.info('Started polling.' + warning)
        self._TeleBot__stop_polling.clear()
        error_interval = 0.25

        polling_thread = util.WorkerThread(name="PollingThread")
        or_event = util.OrEvent(
            polling_thread.done_event,
            polling_thread.exception_event,
            self.worker_pool.exception_event
        )

        while not self._TeleBot__stop_polling.wait(interval):
            or_event.clear()
            try:
                self.handle_timers()
                polling_thread.put(self._TeleBot__retrieve_updates, timeout, long_polling_timeout, allowed_updates=allowed_updates)
                or_event.wait()  # wait for polling thread finish, polling thread error or thread pool error
                polling_thread.raise_exceptions()
                self.worker_pool.raise_exceptions()
                error_interval = 0.25
            except apihelper.ApiException as e:
                if self.exception_handler is not None:
                    handled = self.exception_handler.handle(e)
                else:
                    handled = False
                if not handled:
                    if logger_level and logger_level >= logging.ERROR:
                        logger.error("Threaded polling exception: %s", str(e))
                    if logger_level and logger_level >= logging.DEBUG:
                        logger.error("Exception traceback:\n%s", traceback.format_exc())
                    if not non_stop:
                        self._TeleBot__stop_polling.set()
                        logger.info("Exception occurred. Stopping." + warning)
                    else:
                        logger.info("Waiting for {0} seconds until retry".format(error_interval) + warning)
                        time.sleep(error_interval)
                        if error_interval * 2 < 60:
                            error_interval *= 2
                        else:
                            error_interval = 60
                else:
                    time.sleep(error_interval)
                polling_thread.clear_exceptions()   #*
                self.worker_pool.clear_exceptions() #*
            except KeyboardInterrupt:
                logger.info("KeyboardInterrupt received." + warning)
                self._TeleBot__stop_polling.set()
                break
            except Exception as e:
                if self.exception_handler is not None:
                    handled = self.exception_handler.handle(e)
                else:
                    handled = False
                if not handled:
                    polling_thread.stop()
                    polling_thread.clear_exceptions()   #*
                    self.worker_pool.clear_exceptions() #*
                    raise e
                else:
                    polling_thread.clear_exceptions()
                    self.worker_pool.clear_exceptions()
                    time.sleep(error_interval)

        polling_thread.stop()
        polling_thread.clear_exceptions()
        self.worker_pool.clear_exceptions()
        logger.info('Stopped polling.' + warning)