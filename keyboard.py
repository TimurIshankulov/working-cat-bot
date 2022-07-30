from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import texts
import info

VACUUM_LEVEL = 2
BAKE_LEVEL = 3
TIKTOK_LEVEL = 4
ADVERTISEMENT_LEVEL = 6
CURLING_LEVEL = 10
INVESTOR_LEVEL = 14
PILOT_LEVEL = 18
CONSUL_LEVEL = 22
CEO_LEVEL = 26

class Keyboard:

    @staticmethod
    def get_choose_work_keyboard(user):
        """Returns Inline Keyboard for choosing work"""
        keyboard = InlineKeyboardMarkup()

        if user.level < CURLING_LEVEL:
            inline_wash_dish = InlineKeyboardButton(
                text=texts.WORK_WASH_DISH_DESC.format(
                    round(info.work_timer_dict['wash_dish'] / 60 * user.speed_multiplier)),
                callback_data='wash_dish')
            keyboard.add(inline_wash_dish)

        if user.level >= VACUUM_LEVEL and user.level < INVESTOR_LEVEL:
            inline_vacuum = InlineKeyboardButton(
                text=texts.WORK_VACUUM_DESC.format(
                    round(info.work_timer_dict['vacuum'] / 60 * user.speed_multiplier)),
                callback_data='vacuum')
            keyboard.add(inline_vacuum)

        if user.level >= BAKE_LEVEL and user.level < PILOT_LEVEL:
            inline_bake = InlineKeyboardButton(
                text=texts.WORK_BAKE_DESC.format(
                    round(info.work_timer_dict['bake'] / 60 * user.speed_multiplier)),
                callback_data='bake')
            keyboard.add(inline_bake)
        
        if user.level >= TIKTOK_LEVEL and user.level < CONSUL_LEVEL:
            inline_tiktok = InlineKeyboardButton(
                text=texts.WORK_TIKTOK_DESC.format(
                    round(info.work_timer_dict['tiktok'] / 60 * user.speed_multiplier)),
                callback_data='tiktok')
            keyboard.add(inline_tiktok)

        if user.level >= ADVERTISEMENT_LEVEL and user.level < CEO_LEVEL:
            inline_advertisement = InlineKeyboardButton(
                text=texts.WORK_ADVERTISEMENT_DESC.format(
                    round(info.work_timer_dict['advertisement'] / 60 * user.speed_multiplier)),
                callback_data='advertisement')
            keyboard.add(inline_advertisement)

        if user.level >= CURLING_LEVEL:
            inline_curling = InlineKeyboardButton(
                text=texts.WORK_CURLING_DESC.format(
                    round(info.work_timer_dict['curling'] / 60 * user.speed_multiplier)),
                callback_data='curling')
            keyboard.add(inline_curling)

        if user.level >= INVESTOR_LEVEL:
            inline_investor = InlineKeyboardButton(
                text=texts.WORK_INVESTOR_DESC.format(
                    round(info.work_timer_dict['investor'] / 60 * user.speed_multiplier)),
                callback_data='investor')
            keyboard.add(inline_investor)

        if user.level >= PILOT_LEVEL:
            inline_pilot = InlineKeyboardButton(
                text=texts.WORK_PILOT_DESC.format(
                    round(info.work_timer_dict['pilot'] / 60 * user.speed_multiplier)),
                callback_data='pilot')
            keyboard.add(inline_pilot)

        if user.level >= CONSUL_LEVEL:
            inline_consul = InlineKeyboardButton(
                text=texts.WORK_CONSUL_DESC.format(
                    round(info.work_timer_dict['consul'] / 60 * user.speed_multiplier)),
                callback_data='consul')
            keyboard.add(inline_consul)

        if user.level >= CEO_LEVEL:
            inline_ceo = InlineKeyboardButton(
                text=texts.WORK_CEO_DESC.format(
                    round(info.work_timer_dict['ceo'] / 60 * user.speed_multiplier)),
                callback_data='ceo')
            keyboard.add(inline_ceo)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_work')
        keyboard.add(inline_back)

        return keyboard

    @staticmethod
    def get_choose_toy_keyboard(user):
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

    @staticmethod
    def get_choose_food_keyboard(user):
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

    @staticmethod
    def get_choose_home_keyboard(user):
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

    @staticmethod
    def get_choose_treasure_hunt_keyboard(user):
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
            inline_expedition = InlineKeyboardButton(
                text=texts.TREASURE_HUNT_EXPEDITION_DESC,
                callback_data='expedition')
            keyboard.add(inline_expedition)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_treasure_hunt')
        keyboard.add(inline_back)
        return keyboard

    @staticmethod
    def get_choose_donate_keyboard(user):
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

        inline_furniture = InlineKeyboardButton(
            text=texts.CAT_COMMITTEE_DONATE_FURNITURE,
            callback_data='donate_furniture')
        keyboard.add(inline_furniture)

        inline_back = InlineKeyboardButton(
            text=texts.MENU_BACK,
            callback_data='back_from_choosing_donate')
        keyboard.add(inline_back)
        return keyboard

    @staticmethod
    def get_keyboard(user):
        """Returns keyboard depending on <user.status>"""
        keyboard = ReplyKeyboardMarkup(True, True)
        if user.status == 'idle':
            keyboard.row(texts.MENU_STATUS, texts.MENU_WORK)
            keyboard.row(texts.MENU_TOYS, texts.MENU_FOOD, texts.MENU_HOME)
            keyboard.row(texts.MENU_TREASURE_HUNT, texts.MENU_TROPHIES)
            keyboard.row(texts.MENU_CAT_COMMITTEE)

        elif user.status == 'choose_work':
            keyboard = Keyboard.get_choose_work_keyboard(user)

        elif user.status == 'choose_toys':
            keyboard = Keyboard.get_choose_toy_keyboard(user)

        elif user.status == 'choose_food':
            keyboard = Keyboard.get_choose_food_keyboard(user)

        elif user.status == 'choose_home':
            keyboard = Keyboard.get_choose_home_keyboard(user)

        elif user.status == 'choose_treasure_hunt':
            keyboard = Keyboard.get_choose_treasure_hunt_keyboard(user)

        elif user.status == 'cat_committee':
            keyboard.row(texts.MENU_CAT_COMMITTEE_STATUS, texts.MENU_CAT_COMMITTEE_DONATE)
            keyboard.row(texts.MENU_CAT_COMMITTEE_RATING_EXPERIENCE,
                         texts.MENU_CAT_COMMITTEE_RATING_COINS)
            keyboard.row(texts.MENU_CAT_COMMITTEE_BACK)

        elif user.status == 'choose_donate':
            keyboard = Keyboard.get_choose_donate_keyboard(user)
        
        return keyboard