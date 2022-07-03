import time

import telebot
from telebot.types import ReplyKeyboardMarkup

from models import User
from working_cat_telebot import WorkingCatTeleBot
import utils
import texts
from config import telegram_token

bot = WorkingCatTeleBot(telegram_token)

keyboard_main = ReplyKeyboardMarkup(True, True)
keyboard_main.row('Статус', 'Работа')

@bot.message_handler(commands=['start'])
def start_message(message):
    """Handler for new members"""
    user = User(id=str(message.from_user.id), username=message.from_user.username,
                chat_id=message.chat.id, status='new')
    user.fullname = utils.get_fullname(message.from_user.first_name, message.from_user.last_name)
    user.save()
    bot.send_message(message.chat.id, texts.GREETING_1, reply_markup=None)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    """Handler for callback queries"""
    user_id = str(call.message.chat.id)
    user = bot.get_user(user_id)
    
    if call.message:
        if call.data == 'wash_dish' or call.data == 'vacuum' or call.data == 'bake':
            user.status = 'on_work'
            user.save()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=call.message.text, reply_markup=None)
            if call.data == 'wash_dish':
                reply = texts.WORK_WASH_DISH_STARTED.format(user.cat_name)
                seconds = 60
            elif call.data == 'vacuum':
                reply = texts.WORK_VACUUM_STARTED.format(user.cat_name)
                seconds = 5
            elif call.data == 'bake':
                reply = texts.WORK_BAKE_STARTED.format(user.cat_name)
                seconds = 5
            keyboard = bot.get_keyboard(user.status)
            bot.send_message(call.message.chat.id, reply, reply_markup=keyboard)
            bot.add_timer(user, call.message.chat.id, call.message.message_id, int(time.time()), seconds)

        elif call.data == 'back_from_choosing_work':
            user.status = 'idle'
            user.save()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=call.message.text, reply_markup=None)
            reply = texts.WORK_BACK_TO_MAIN_MENU
            keyboard = bot.get_keyboard(user.status)
            bot.send_message(call.message.chat.id, reply, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    """Handler for text messages from users"""
    user_id = str(message.from_user.id)
    user = bot.get_user(user_id)

    if user.status == 'new':
        user.cat_name = message.text
        user.status = 'idle'
        user.save()
        reply = texts.GREETING_2.format(user.cat_name)
        keyboard = bot.get_keyboard(user.status)
        bot.send_message(message.chat.id, reply, reply_markup=keyboard)

    elif user.status == 'idle':
        if message.text.lower() == 'статус':
            reply = texts.STATUS_OVERALL.format(user.cat_name, texts.STATUS_IDLE, user.level,
                                                user.experience, user.until_level)
            keyboard = bot.get_keyboard(user.status)
            bot.send_message(message.chat.id, reply, reply_markup=keyboard)

        elif message.text.lower() == 'работа':
            user.status = 'choose_work'
            user.save()
            reply = texts.CHOOSE_WORK
            keyboard = bot.get_keyboard(user.status)
            bot.send_message(message.chat.id, reply, reply_markup=keyboard)

    elif user.status == 'on_work':
        if message.text.lower() == 'статус':
            reply = texts.STATUS_OVERALL.format(user.cat_name, texts.STATUS_ON_WORK, user.level,
                                                user.experience, user.until_level)
            keyboard = bot.get_keyboard(user.status)
            bot.send_message(message.chat.id, reply, reply_markup=keyboard)

        elif message.text.lower() == 'работа':
            user.status = 'choose_work'
            user.save()
            reply = texts.CHOOSE_WORK
            keyboard = bot.get_keyboard(user.status)
            bot.send_message(message.chat.id, reply, reply_markup=keyboard)
        #user.status = 'idle'
        #user.save()
        #reply = texts.WORK_DONE.format(user.cat_name)
        #keyboard = bot.get_keyboard(user.status)
        #bot.send_message(message.chat.id, reply, reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, texts.REPLY_UNKNOWN_STATUS)


bot.polling(non_stop=True)