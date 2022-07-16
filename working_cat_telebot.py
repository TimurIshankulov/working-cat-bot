import pickle
import datetime
import time
import logging
import traceback
import random
import sys

from sqlitedict import SqliteDict
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telebot import apihelper, util, types
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Timer, User, CatCommittee, DeclarativeBase
from config import log_file, sqlite_users, sqlite_timers, sqlite_cat_committee, conn_string
import texts
import info
import utils

random.seed()
logger = logging.getLogger('TeleBot')

fill='█'
zfill='░'
fill_len = 15

engine_working_cat = create_engine(conn_string)
DeclarativeBase.metadata.bind = engine_working_cat
DBSession_working_cat = sessionmaker(bind=engine_working_cat)
db_session = DBSession_working_cat()

class WorkingCatTeleBot(TeleBot):

    def __init__(self, token, threaded=True, skip_pending=False, num_threads=1):
        TeleBot.__init__(self, token=token, threaded=threaded,
                         skip_pending=skip_pending, num_threads=num_threads)

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
        user_id = str(user_id)
        db_session = DBSession_working_cat()
        try:
            user = db_session.query(User).filter_by(id=user_id).first()
            user.trophies = pickle.loads(user.trophies)
            return user
        except Exception:
            print(sys.exc_info()[1])
        finally:
            db_session.close()

    def get_cat_committee(self):
        db_session = DBSession_working_cat()
        try:
            cat_committee = db_session.query(CatCommittee).filter_by(id='cat_committee').first()
            if cat_committee is not None:
                return cat_committee
            else:
                return CatCommittee()
        except Exception:
            print(sys.exc_info()[1])
        finally:
            db_session.close()

    def get_choose_work_keyboard(self, user):
        """Returns Inline Keyboard for choosing work"""
        keyboard = InlineKeyboardMarkup()

        inline_wash_dish = InlineKeyboardButton(
            text=texts.WORK_WASH_DISH_DESC.format(
                round(info.work_timer_dict['wash_dish'] / 60 * user.speed_multiplier)),
            callback_data='wash_dish')
        keyboard.add(inline_wash_dish)

        if user.level >= 2:
            inline_vacuum = InlineKeyboardButton(
                text=texts.WORK_VACUUM_DESC.format(
                    round(info.work_timer_dict['vacuum'] / 60 * user.speed_multiplier)),
                callback_data='vacuum')
            keyboard.add(inline_vacuum)

        if user.level >= 3:
            inline_bake = InlineKeyboardButton(
                text=texts.WORK_BAKE_DESC.format(
                    round(info.work_timer_dict['bake'] / 60 * user.speed_multiplier)),
                callback_data='bake')
            keyboard.add(inline_bake)
        
        if user.level >= 4:
            inline_tiktok = InlineKeyboardButton(
                text=texts.WORK_TIKTOK_DESC.format(
                    round(info.work_timer_dict['tiktok'] / 60 * user.speed_multiplier)),
                callback_data='tiktok')
            keyboard.add(inline_tiktok)

        if user.level >= 5:
            inline_advertisement = InlineKeyboardButton(
                text=texts.WORK_ADVERTISEMENT_DESC.format(
                    round(info.work_timer_dict['advertisement'] / 60 * user.speed_multiplier)),
                callback_data='advertisement')
            keyboard.add(inline_advertisement)
        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_work')
        keyboard.add(inline_back)
        return keyboard

    def get_choose_toy_keyboard(self, user):
        """Returns Inline Keyboard for choosing toy"""
        keyboard = InlineKeyboardMarkup()

        inline_mouse = InlineKeyboardButton(
            text=texts.TOYS_MOUSE_DESC,
            callback_data='toy_mouse')
        keyboard.add(inline_mouse)

        if user.level >= 5:
            inline_bow = InlineKeyboardButton(
                text=texts.TOYS_BOW_DESC,
                callback_data='toy_bow')
            keyboard.add(inline_bow)

        if user.level >= 10:
            inline_ball = InlineKeyboardButton(
                text=texts.TOYS_BALL_DESC,
                callback_data='toy_ball')
            keyboard.add(inline_ball)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_toy')
        keyboard.add(inline_back)
        return keyboard

    def get_choose_food_keyboard(self, user):
        """Returns Inline Keyboard for choosing food"""
        keyboard = InlineKeyboardMarkup()

        inline_fish = InlineKeyboardButton(
            text=texts.FOOD_FISH_DESC,
            callback_data='food_fish')
        keyboard.add(inline_fish)

        if user.level >= 5:
            inline_premium = InlineKeyboardButton(
                text=texts.FOOD_PREMIUM_DESC,
                callback_data='food_premium')
            keyboard.add(inline_premium)

        if user.level >= 10:
            inline_shrimp = InlineKeyboardButton(
                text=texts.FOOD_SHRIMP_DESC,
                callback_data='food_shrimp')
            keyboard.add(inline_shrimp)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_food')
        keyboard.add(inline_back)
        return keyboard

    def get_choose_home_keyboard(self, user):
        """Returns Inline Keyboard for choosing home"""
        keyboard = InlineKeyboardMarkup()

        if user.level >= 5:
            inline_small = InlineKeyboardButton(
                text=texts.HOME_SMALL_DESC.format(info.home_coin_cost_dict['home_small'],
                                                  info.home_gem_cost_dict['home_small']),
                callback_data='home_small')
            keyboard.add(inline_small)

        if user.level >= 10:
            inline_flat = InlineKeyboardButton(
                text=texts.HOME_FLAT_DESC.format(info.home_coin_cost_dict['home_flat'],
                                                 info.home_gem_cost_dict['home_flat']),
                callback_data='home_flat')
            keyboard.add(inline_flat)

        if user.level >= 15:
            inline_house = InlineKeyboardButton(
                text=texts.HOME_HOUSE_DESC.format(info.home_coin_cost_dict['home_house'],
                                                  info.home_gem_cost_dict['home_house']),
                callback_data='home_house')
            keyboard.add(inline_house)

        if user.level >= 20:
            inline_mansion = InlineKeyboardButton(
                text=texts.HOME_MANSION_DESC.format(info.home_coin_cost_dict['home_mansion'],
                                                    info.home_gem_cost_dict['home_mansion']),
                callback_data='home_mansion')
            keyboard.add(inline_mansion)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_home')
        keyboard.add(inline_back)
        return keyboard

    def get_choose_treasure_hunt_keyboard(self, user):
        """Returns Inline Keyboard for choosing treasure hunt"""
        keyboard = InlineKeyboardMarkup()

        if user.level >= 5:
            inline_solo = InlineKeyboardButton(
                text=texts.TREASURE_HUNT_SOLO_DESC,
                callback_data='solo')
            keyboard.add(inline_solo)

        if user.level >= 10:
            inline_treasure = InlineKeyboardButton(
                text=texts.TREASURE_HUNT_TREASURE_DESC,
                callback_data='treasure')
            keyboard.add(inline_treasure)

        if user.level >= 15:
            inline_expredition = InlineKeyboardButton(
                text=texts.TREASURE_HUNT_EXPEDITION_DESC,
                callback_data='expedition')
            keyboard.add(inline_expredition)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_treasure_hunt')
        keyboard.add(inline_back)
        return keyboard

    def get_choose_donate_keyboard(self, user):
        keyboard = InlineKeyboardMarkup()

        inline_tea = InlineKeyboardButton(
            text=texts.CAT_COMMITTEE_DONATE_TEA,
            callback_data='donate_tea')
        keyboard.add(inline_tea)

        inline_paper = InlineKeyboardButton(
            text=texts.CAT_COMMITTEE_DONATE_PAPER,
            callback_data='donate_paper')
        keyboard.add(inline_paper)

        inline_renovation = InlineKeyboardButton(
            text=texts.CAT_COMMITTEE_DONATE_RENOVATION,
            callback_data='donate_renovation')
        keyboard.add(inline_renovation)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_donate')
        keyboard.add(inline_back)
        return keyboard

    def get_keyboard(self, user):
        """Returns keyboard depending on <user.status>"""
        keyboard = ReplyKeyboardMarkup(True, True)
        if user.status == 'idle':
            keyboard.row(texts.MENU_STATUS, texts.MENU_WORK)
            keyboard.row(texts.MENU_TOYS, texts.MENU_FOOD, texts.MENU_HOME)
            keyboard.row(texts.MENU_TREASURE_HUNT, texts.MENU_TROPHIES)
            keyboard.row(texts.MENU_CAT_COMMITTEE)

        elif user.status == 'choose_work':
            keyboard = self.get_choose_work_keyboard(user)

        elif user.status == 'choose_toys':
            keyboard = self.get_choose_toy_keyboard(user)

        elif user.status == 'choose_food':
            keyboard = self.get_choose_food_keyboard(user)

        elif user.status == 'choose_home':
            keyboard = self.get_choose_home_keyboard(user)

        elif user.status == 'choose_treasure_hunt':
            keyboard = self.get_choose_treasure_hunt_keyboard(user)

        elif user.status == 'cat_committee':
            keyboard.row(texts.MENU_CAT_COMMITTEE_STATUS, texts.MENU_CAT_COMMITTEE_DONATE)
            keyboard.row(texts.MENU_CAT_COMMITTEE_RATING, texts.MENU_CAT_COMMITTEE_BACK)

        elif user.status == 'choose_donate':
            keyboard = self.get_choose_donate_keyboard(user)
        
        return keyboard

    def action_add_new_user(self, message):
        """Adds new user to the database"""
        user = User(id=str(message.from_user.id), username=message.from_user.username,
                    chat_id=message.chat.id, status='new')
        user.fullname = utils.get_fullname(message.from_user.first_name, message.from_user.last_name)
        user.save()
        self.send_message(message.chat.id, texts.GREETING_1, reply_markup=None)

    def action_get_cat_name(self, user, message):
        """Saves cat_name and sends wellcome message"""
        user.cat_name = message.text
        user.status = 'idle'
        user.save()
        reply = texts.GREETING_2.format(user.cat_name)
        keyboard = self.get_keyboard(user)
        self.send_message(message.chat.id, reply, reply_markup=keyboard)

    def action_send_status(self, user, chat_id):
        """Sends status to user"""
        user.status = 'idle'
        user.save()
        if user.is_working:
            text = texts.CAT_STATUS_ON_WORK
        elif user.is_treasure_hunting:
            text = texts.CAT_STATUS_ON_TREASURE_HUNT
        else:
            text = texts.CAT_STATUS_IDLE
        reply = texts.STATUS_OVERALL.format(user.cat_name, user.level, text,
                                            user.experience, user.until_level,
                                            user.coins, user.gems)
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_send_trophies(self, user, chat_id):
        """Sends the trophies list to user"""
        user.status = 'idle'
        user.save()

        reply = ''
        for key in user.trophies.keys():
            if user.trophies[key]:
                reply += texts.TROPHIES_DICT[key] + '\n'
            else:
                reply += texts.TROPHY_UNKNOWN + '\n'

        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_unknown_status(self, user, chat_id):
        """Sends a message with error and changes the status to idle"""
        user.status = 'idle'
        user.save()
        reply = texts.REPLY_UNKNOWN_STATUS
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_choose_work(self, user, chat_id):
        """Sends message with work choices"""
        user.status = 'choose_work'
        user.save()
        reply = texts.WORK_CHOOSE_WORK
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_choose_toys(self, user, chat_id):
        """Sends message with toy choices"""
        user.status = 'choose_toys'
        user.save()
        reply = texts.TOYS_CHOOSE_TOY
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_choose_food(self, user, chat_id):
        """Sends message with food choices"""
        user.status = 'choose_food'
        user.save()
        reply = texts.FOOD_CHOOSE_FOOD
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_choose_home(self, user, chat_id):
        """Sends message with home choices"""
        if user.level >= 5:
            user.status = 'choose_home'
            user.save()
            reply = texts.HOME_CHOOSE_HOME
            keyboard = self.get_keyboard(user)
            self.send_message(chat_id, reply, reply_markup=keyboard)
        else:
            user.status = 'idle'
            user.save()
            reply = texts.HOME_LOW_LEVEL
            keyboard = self.get_keyboard(user)
            self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_choose_treasure_hunt(self, user, chat_id):
        """Sends message with treasure hunt choices"""
        if user.level >= 5:
            user.status = 'choose_treasure_hunt'
            user.save()
            reply = texts.TREASURE_HUNT_CHOOSE_TREASURE_HUNT
            keyboard = self.get_keyboard(user)
            self.send_message(chat_id, reply, reply_markup=keyboard)
        else:
            user.status = 'idle'
            user.save()
            reply = texts.TREASURE_HUNT_LOW_LEVEL
            keyboard = self.get_keyboard(user)
            self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_callback_acquire_toy(self, user, call):
        """Tries to acquire a toy, sends result message"""
        toy_acquired = False
        insufficient_coins = False
        user.status = 'idle'
        user.save()
        toy = call.data
        toy_cost = info.toy_cost_dict[toy]
        
        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)

        if call.data == 'toy_mouse' and not user.toy_mouse_acquired:
            if user.coins >= toy_cost:
                user.coins -= toy_cost
                user.toy_mouse_acquired = True
                toy_acquired = True
            else:
                insufficient_coins = True

        if call.data == 'toy_bow' and not user.toy_bow_acquired:
            if user.coins >= toy_cost:
                user.coins -= toy_cost
                user.toy_bow_acquired = True
                toy_acquired = True
            else:
                insufficient_coins = True

        if call.data == 'toy_ball' and not user.toy_ball_aquired:
            if user.coins >= toy_cost:
                user.coins -= toy_cost
                user.toy_ball_acquired = True
                toy_acquired = True
            else:
                insufficient_coins = True
        user.save()

        if toy_acquired:
            reply = texts.TOYS_KIND_DICT[call.data]
            keyboard = self.get_keyboard(user)
            self.send_message(call.message.chat.id, reply, reply_markup=keyboard)
        else:
            if insufficient_coins:
                reply = texts.TOYS_INSUFFICIENT_COINS
                keyboard = self.get_keyboard(user)
                self.send_message(call.message.chat.id, reply, reply_markup=keyboard)
            else:    
                reply = texts.TOYS_ALREADY_ACQUIRED
                keyboard = self.get_keyboard(user)
                self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

    def action_callback_acquire_food(self, user, call):
        """Tries to acquire food, sends result message"""
        food_acquired = False
        insufficient_coins = False
        user.status = 'idle'
        user.save()
        food = call.data
        food_cost = info.food_cost_dict[food]
        
        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)
        
        if food == 'food_fish' and not user.food_fish_acquired:
            if user.coins >= food_cost:
                user.coins -= food_cost
                user.food_fish_acquired = True
                food_acquired = True
            else:
                insufficient_coins = True
        elif food == 'food_premium' and not user.food_premium_acquired:
            if user.coins >= food_cost:
                user.coins -= food_cost
                user.food_premium_acquired = True
                food_acquired = True
            else:
                insufficient_coins = True
        elif food == 'food_shrimp' and not user.food_shrimp_acquired:
            if user.coins >= food_cost:
                user.coins -= food_cost
                user.food_shrimp_acquired = True
                food_acquired = True
            else:
                insufficient_coins = True
        user.save()

        if food_acquired:
            reply = texts.FOOD_KIND_DICT[food]
            keyboard = self.get_keyboard(user)
            self.send_message(call.message.chat.id, reply, reply_markup=keyboard)
        else:
            if insufficient_coins:
                reply = texts.FOOD_INSUFFICIENT_COINS
                keyboard = self.get_keyboard(user)
                self.send_message(call.message.chat.id, reply, reply_markup=keyboard)
            else:
                reply = texts.FOOD_ALREADY_ACQUIRED
                keyboard = self.get_keyboard(user)
                self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

    def action_callback_acquire_home(self, user, call):
        """Tries to acquire home, sends result message"""
        home_acquired = False
        insufficient_coins = False
        insufficient_gems = False
        user.status = 'idle'
        user.save()
        home = call.data
        home_coin_cost = info.home_coin_cost_dict[home]
        home_gem_cost = info.home_gem_cost_dict[home]

        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)
        
        if home == 'home_small' and not user.home_small_acquired:
            if user.coins >= home_coin_cost:
                if user.gems >= home_gem_cost:
                    user.coins -= home_coin_cost
                    user.gems -= home_gem_cost
                    user.home_small_acquired = True
                    home_acquired = True
                else:
                    insufficient_gems = True
            else:
                insufficient_coins = True

        elif home == 'home_flat' and not user.home_flat_acquired:
            if user.coins >= home_coin_cost:
                if user.gems >= home_gem_cost:
                    user.coins -= home_coin_cost
                    user.gems -= home_gem_cost
                    user.home_flat_acquired = True
                    home_acquired = True
                else:
                    insufficient_gems = True
            else:
                insufficient_coins = True

        elif home == 'home_house' and not user.home_house_acquired:
            if user.coins >= home_coin_cost:
                if user.gems >= home_gem_cost:
                    user.coins -= home_coin_cost
                    user.gems -= home_gem_cost
                    user.home_house_acquired = True
                    home_acquired = True
                else:
                    insufficient_gems = True
            else:
                insufficient_coins = True

        elif home == 'home_mansion' and not user.home_mansion_acquired:
            if user.coins >= home_coin_cost:
                if user.gems >= home_gem_cost:
                    user.coins -= home_coin_cost
                    user.gems -= home_gem_cost
                    user.home_mansion_acquired = True
                    home_acquired = True
                else:
                    insufficient_gems = True
            else:
                insufficient_coins = True
        user.save()

        if home_acquired:
            reply = texts.HOME_KIND_DICT[home]
        elif insufficient_coins:
            reply = texts.HOME_INSUFFICIENT_COINS
        elif insufficient_gems:
            reply = texts.HOME_INSUFFICIENT_GEMS
        else:
            reply = texts.HOME_ALREADY_ACQUIRED

        keyboard = self.get_keyboard(user)
        self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

    def action_callback_back_from_submenu(self, user, call):
        """Returns to main menu from any submenu"""
        user.status = 'idle'
        user.save()
        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)
        reply = texts.BACK_TO_MAIN_MENU
        keyboard = self.get_keyboard(user)
        self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

    def action_callback_take_work(self, user, call):
        """Assigns cat for work"""
        user.status = 'idle'
        user.save()
        if user.is_working:
            reply = texts.WORK_ALREADY_WORKING.format(user.cat_name)
            keyboard = self.get_keyboard(user)
            self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   text=call.message.text, reply_markup=None)
            self.send_message(call.message.chat.id, reply, reply_markup=keyboard)
            return
        user.is_working = True
        user.current_work = call.data
        user.save()
        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)

        reply = texts.WORK_KIND_DICT[call.data].format(user.cat_name)
        keyboard = self.get_keyboard(user)
        self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

        seconds = round(info.work_timer_dict[call.data] * user.speed_multiplier)
        self.add_timer(user=user,
                       chat_id=call.message.chat.id,
                       message_id=call.message.message_id,
                       start_timestamp=int(time.time()),
                       seconds=seconds,
                       timer_type='work')

    def action_complete_work(self, user, timer):
        """Completes active work, removes timer message, sends result message"""
        self.delete_message(chat_id=timer.chat_id,
                            message_id=timer.message_id)
        reply = texts.WORK_DONE.format(
            user.cat_name,
            info.work_experience_dict[user.current_work] * user.experience_multiplier,
            info.work_coins_dict[user.current_work] * user.coins_multiplier)
        keyboard = self.get_keyboard(user)
        self.send_message(timer.chat_id, reply, reply_markup=keyboard)

        experience = info.work_experience_dict[user.current_work] * user.experience_multiplier
        coins = info.work_coins_dict[user.current_work] * user.coins_multiplier
        user.experience += experience
        user.experience_donated += experience
        user.coins += coins
        user.is_working = False
        user.current_work = None
        user.save()

        cat_committee = self.get_cat_committee()
        cat_committee.experience += experience
        cat_committee.save()

        self.remove_timer(timer)

    def action_callback_start_treasure_hunt(self, user, call):
        """Assigns cat for treasure hunt"""
        user.status = 'idle'
        user.save()
        if user.is_treasure_hunting:
            reply = texts.TREASURE_HUNT_ALREADY_HUNTING.format(user.cat_name)
            keyboard = self.get_keyboard(user)
            self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   text=call.message.text, reply_markup=None)
            self.send_message(call.message.chat.id, reply, reply_markup=keyboard)
            return None
        user.is_treasure_hunting = True
        user.current_treasure_hunt = call.data
        user.save()
        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)

        reply = texts.TREASURE_HUNT_KIND_DICT[call.data].format(user.cat_name)
        keyboard = self.get_keyboard(user)
        self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

        seconds = info.treasure_hunt_timer_dict[call.data]
        self.add_timer(user=user,
                       chat_id=call.message.chat.id,
                       message_id=call.message.message_id,
                       start_timestamp=int(time.time()),
                       seconds=seconds,
                       timer_type='treasure_hunt')

    def action_complete_treasure_hunt(self, user, timer):
        """Completes active treasure hunt, removes timer message, sends result message"""
        self.delete_message(chat_id=timer.chat_id,
                            message_id=timer.message_id)
        # Calculate rewards
        treasure_chance = random.randint(1, 100)
        if treasure_chance <= 80:
            gems_target = info.treasure_hunt_gems_dict[user.current_treasure_hunt]
            gems_reward = random.randint(gems_target - 1, gems_target + 1)
            coins_min = int(info.treasure_hunt_coins_dict[user.current_treasure_hunt] * 0.7)
            coins_max = int(info.treasure_hunt_coins_dict[user.current_treasure_hunt] * 1.3)
            coins_reward = random.randint(coins_min, coins_max)

            # Check if trophy found
            trophies_to_roll = {key:value for key, value in user.trophies.items() if value == False}
            if len(trophies_to_roll) > 0:
                trophy_chance = random.randint(1, 100)
                if trophy_chance <= 40:
                    trophy = random.choice(list(trophies_to_roll.keys()))
                    user.trophies[trophy] = True
                    reply = texts.TROPHY_AQUIRED.format(texts.TROPHIES_DICT[trophy])
                    self.send_message(timer.chat_id, reply)

            reply = texts.TREASURE_HUNT_DONE.format(user.cat_name,
                                                    coins_reward * user.coins_multiplier,
                                                    gems_reward)
            keyboard = self.get_keyboard(user)
            self.send_message(timer.chat_id, reply, reply_markup=keyboard)

            user.coins += coins_reward * user.coins_multiplier
            user.gems += gems_reward
            user.save()
        else:
            reply = texts.TREASURE_HUNT_FAILED
            keyboard = self.get_keyboard(user)
            self.send_message(timer.chat_id, reply, reply_markup=keyboard)

        user.is_treasure_hunting = False
        user.current_treasure_hunt = None
        user.save()

        self.remove_timer(timer)

    def action_send_cat_committee_greeting(self, user, chat_id):
        """Sends status of the cat committee"""
        user.status = 'cat_committee'
        user.save()

        reply = texts.CAT_COMMITTEE_GREETING
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_callback_to_cat_committee_menu(self, user, call):
        """Returns to Cat Committee menu from submenu"""
        user.status = 'cat_committee'
        user.save()
        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)
        reply = texts.MENU_CAT_COMMITTEE_TO_MENU
        keyboard = self.get_keyboard(user)
        self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

    def action_send_cat_committee_status(self, user, chat_id):
        """Sends status of the cat committee"""
        user.status = 'cat_committee'
        user.save()

        cat_committee = self.get_cat_committee()

        reply = texts.CAT_COMMITTEE_STATUS.format(cat_committee.level,
                                                  cat_committee.experience,
                                                  cat_committee.until_level,
                                                  cat_committee.coins)
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_choose_donate(self, user, chat_id):
        """Sends message with donate choices"""
        user.status = 'choose_donate'
        user.save()
        reply = texts.CAT_COMMITTEE_CHOOSE_DONATE
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_callback_donate_coins(self, user, call):
        """Gives coins away to the Cat Committee"""
        insufficient_coins = False
        donate_successful = False
        user.status = 'cat_committee'
        user.save()        

        self.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               text=call.message.text, reply_markup=None)

        donate = call.data
        donate_coin_cost = info.donate_cost_dict[donate]

        if user.coins >= donate_coin_cost:
            user.coins -= donate_coin_cost
            user.coins_donated += donate_coin_cost
            user.save()

            cat_committee = self.get_cat_committee()
            cat_committee.coins += donate_coin_cost
            cat_committee.save()
            donate_successful = True
        else:
            insufficient_coins = True

        if donate_successful:
            reply = texts.CAT_COMMITTEE_DONATE_SUCCESSFUL.format(donate_coin_cost)
        elif insufficient_coins:
            reply = texts.CAT_COMMITTEE_INSUFFICIENT_COINS
        else:
            reply = texts.CAT_COMMITTEE_ERROR_OCCURRED

        keyboard = self.get_keyboard(user)
        self.send_message(call.message.chat.id, reply, reply_markup=keyboard)

    def action_send_rating(self, user, chat_id):
        """Sends rating table with top donaters"""
        db_session = DBSession_working_cat()
        user.status = 'cat_committee'
        user.save()
        users = db_session.query(User).all()
        rating = []
        for user in users:
            rating.append([user.cat_name,
                           user.experience_donated,
                           user.coins_donated])
        if len(rating) < 10:
            for _ in range(len(rating), 10):
                rating.append([texts.RATING_UNKNOWN_PLAYER, 0, 0])

        rating = sorted(rating, key=lambda x: x[2], reverse=True)
        reply = texts.RATING_TABLE.format(x=rating[:10])
        reply += texts.RATING_YOU_RATING.format(user.experience_donated, user.coins_donated)
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard, parse_mode='Markdown')

    def action_back_from_cat_committee(self, user, chat_id):
        """Back from Cat Committee menu to the main menu"""
        user.status = 'idle'
        user.save()

        reply = texts.BACK_TO_MAIN_MENU
        keyboard = self.get_keyboard(user)
        self.send_message(chat_id, reply, reply_markup=keyboard)

    def action_edit_timer(self, timer, current_timestamp):
        """Edits timer message"""
        progress = int(((current_timestamp - timer.start_timestamp) / 
                         timer.seconds * 100) / (100 / fill_len))
        remains = timer.start_timestamp + timer.seconds - current_timestamp
        str_remains = self.get_time_format(remains)

        if timer.timer_type == 'work':
            reply = texts.WORK_STRING_WORKING
        elif timer.timer_type == 'treasure_hunt':
            reply = texts.TREASURE_HUNT_STRING_HUNTING
        reply += fill * progress + zfill * (fill_len - progress) + '\n'
        reply += str_remains
        self.edit_message_text(chat_id=timer.chat_id,
                               message_id=timer.message_id,
                               text=reply, reply_markup=None)

    def get_time_format(self, timestamp):
        """Returns formatted string with timer remains"""
        mins = str(timestamp // 60) if timestamp // 60 > 9 else '0' + str(timestamp // 60)
        secs = str(timestamp % 60) if timestamp % 60 > 9 else '0' + str(timestamp % 60)
        return '{0}:{1}'.format(mins, secs)

    def remove_timer(self, timer):
        """Removes active timer"""
        db_session = DBSession_working_cat()
        timer_to_delete = db_session.query(Timer).filter_by(id=timer.id).first()
        db_session.delete(timer_to_delete)
        db_session.commit()
        db_session.close()

    def add_timer(self, user, chat_id, message_id, start_timestamp, seconds, timer_type):
        """Adds timer to the database, it will be handled by handle_timers()"""
        timer = Timer(id=None, user=user, chat_id=chat_id, message_id=message_id,
                      start_timestamp=start_timestamp, seconds=seconds, timer_type=timer_type)
        
        timer.save()

    def handle_timers(self):
        """Handles active timers, sends it to users"""
        current_timestamp = int(time.time())
        db_session = DBSession_working_cat()
        timers = db_session.query(Timer).all()
        
        for timer in timers[::1]:
            user = pickle.loads(timer.user)
            if (current_timestamp - timer.start_timestamp >= timer.seconds and
                timer.timer_type == 'work'):
                self.action_complete_work(user, timer)
            elif (current_timestamp - timer.start_timestamp >= timer.seconds and
                  timer.timer_type == 'treasure_hunt'):
                  self.action_complete_treasure_hunt(user, timer)
            else:
                self.action_edit_timer(timer, current_timestamp)
        db_session.close()
    
    def _TeleBot__threaded_polling(self, non_stop=False, interval=0, timeout=None,
                                   long_polling_timeout=None,
                                   logger_level=logging.ERROR, allowed_updates=None):
        if not(logger_level) or (logger_level < logging.INFO):
            warning = '\n  Warning: this message appearance will be changed.\
                Set logger_level=logging.INFO to continue seeing it.'
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
                polling_thread.put(self._TeleBot__retrieve_updates, timeout,
                                   long_polling_timeout, allowed_updates=allowed_updates)
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
                polling_thread.clear_exceptions()
                self.worker_pool.clear_exceptions()
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
                    polling_thread.clear_exceptions()
                    self.worker_pool.clear_exceptions()
                    raise e
                else:
                    polling_thread.clear_exceptions()
                    self.worker_pool.clear_exceptions()
                    time.sleep(error_interval)

        polling_thread.stop()
        polling_thread.clear_exceptions()
        self.worker_pool.clear_exceptions()
        logger.info('Stopped polling.' + warning)