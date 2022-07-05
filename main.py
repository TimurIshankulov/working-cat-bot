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
    """Handler for new users"""
    bot.action_add_new_user(message)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    """Handler for callback queries"""
    user_id = str(call.message.chat.id)
    user = bot.get_user(user_id)
    
    if call.message:
        if (call.data == 'wash_dish' or call.data == 'vacuum' or call.data == 'bake' or
            call.data == 'tiktok' or call.data == 'advertisement'):
            bot.action_callback_take_work(user, call)

        elif call.data == 'back_from_choosing_work':
            bot.action_callback_back_from_submenu(user, call)

        elif call.data == 'toy_mouse' or call.data == 'toy_bow' or call.data == 'toy_ball':
            bot.action_callback_acquire_toy(user, call)

        elif call.data == 'back_from_choosing_toy':
            bot.action_callback_back_from_submenu(user, call)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    """Handler for text messages from users"""
    user_id = str(message.from_user.id)
    user = bot.get_user(user_id)

    if user.status == 'new':
        bot.action_get_cat_name(user, message)

    elif user.status == 'idle':
        if message.text.lower() == 'статус':
            bot.action_send_status(user, message.chat.id)

        elif message.text.lower() == 'работа':
            bot.action_choose_work(user, message.chat.id)

        elif message.text.lower() == 'игрушки':
            bot.action_choose_toys(user, message.chat.id)

        elif message.text.lower() == 'корм':
            bot.action_choose_food(user, message.chat.id)

    elif user.status == 'on_work':
        if message.text.lower() == 'статус':
            bot.action_send_status(user, message.chat.id)

    else:
        bot.action_unknown_status(user, message.chat.id)


bot.polling(non_stop=True, timeout=5, long_polling_timeout=5)