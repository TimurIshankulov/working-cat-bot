import datetime
import shelve

from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from models import User
from config import log_file, shelve_users
import texts

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
            inline_wash_dish = InlineKeyboardButton(text='Мыть посуду', callback_data='wash_dish')
            keyboard.add(inline_wash_dish)
            inline_bake = InlineKeyboardButton(text='Выпекать шарлотку', callback_data='bake')
            keyboard.add(inline_bake)
            inline_vacuum = InlineKeyboardButton(text='Пропылесосить', callback_data='vacuum')
            keyboard.add(inline_vacuum)
            inline_back = InlineKeyboardButton(text='Назад', callback_data='back_from_stop_quest_confirmation')
            keyboard.add(inline_back)
        
        return keyboard
    
