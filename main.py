import sys
sys.stderr = open('working-cat.log', 'w')
import time

import telebot
from telebot.types import ReplyKeyboardMarkup

from models import User
from working_cat_telebot import WorkingCatTeleBot
import utils
import texts
import info
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
        if call.data in ['wash_dish', 'vacuum', 'bake', 'tiktok', 'advertisement',
                         'curling', 'pilot', 'consul']:
            bot.action_callback_take_work(user, call)

        elif call.data in ['toy_mouse', 'toy_bow', 'toy_ball']:
            bot.action_callback_acquire_toy(user, call)

        elif call.data in ['food_fish', 'food_premium', 'food_shrimp']:
            bot.action_callback_acquire_food(user, call)

        elif call.data in ['home_small', 'home_flat', 'home_house', 'home_mansion']:
            bot.action_callback_acquire_home(user, call)

        elif call.data in ['solo', 'treasure', 'expedition']:
            bot.action_callback_start_treasure_hunt(user, call)

        elif call.data in ['donate_tea', 'donate_paper', 'donate_renovation',
                           'donate_furniture']:
            bot.action_callback_donate_coins(user, call)

        elif call.data in ['back_from_choosing_work', 'back_from_choosing_toy',
                           'back_from_choosing_food', 'back_from_choosing_home',
                           'back_from_choosing_treasure_hunt']:
            bot.action_callback_back_from_submenu(user, call)

        elif call.data == 'back_from_choosing_donate':
            bot.action_callback_to_cat_committee_menu(user, call)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    """Handler for text messages from users"""
    user_id = str(message.from_user.id)
    user = bot.get_user(user_id)

    if user.status == 'new':
        bot.action_get_cat_name(user, message)

    elif user.status in info.statuses_for_main_menu:
        if message.text.lower() == 'статус':
            bot.action_send_status(user, message.chat.id)

        elif message.text.lower() == 'работа':
            bot.action_choose_work(user, message.chat.id)

        elif message.text.lower() == 'игрушки':
            bot.action_choose_toys(user, message.chat.id)

        elif message.text.lower() == 'корм':
            bot.action_choose_food(user, message.chat.id)

        elif message.text.lower() == 'дома':
            bot.action_choose_home(user, message.chat.id)

        elif message.text.lower() == 'поиск сокровищ':
            bot.action_choose_treasure_hunt(user, message.chat.id)

        elif message.text.lower() == 'трофеи':
            bot.action_send_trophies(user, message.chat.id)

        elif message.text.lower() == 'котовский комитет':
            bot.action_send_cat_committee_greeting(user, message.chat.id)

        elif message.text.lower() == 'котик в отпуске':
            bot.action_send_status(user, message.chat.id)
    
    elif user.status in info.statuses_for_cat_committee_menu:
        if message.text.lower() == 'статус комитета':
            bot.action_send_cat_committee_status(user, message.chat.id)

        elif message.text.lower() == 'пожертвовать монеты':
            bot.action_choose_donate(user, message.chat.id)

        elif message.text.lower() == 'рейтинг по опыту':
            bot.action_send_rating(user, message.chat.id, 'experience')

        elif message.text.lower() == 'рейтинг по монетам':
            bot.action_send_rating(user, message.chat.id, 'coins')

        elif message.text.lower() == 'назад':
            bot.action_back_from_cat_committee(user, message.chat.id)

    else:
        bot.action_unknown_status(user, message.chat.id)


while True:
    try:
        bot.polling(non_stop=True, timeout=5, long_polling_timeout=5)
    except Exception:
        print('Exception occurred:')
        print(sys.exc_info()[1])
        time.sleep(10)