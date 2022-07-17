import pickle

from sqlitedict import SqliteDict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import CatCommittee, User, DeclarativeBase

from config import telegram_token, conn_string
from config import sqlite_users, sqlite_cat_committee

engine_working_cat = create_engine(conn_string)
DeclarativeBase.metadata.bind = engine_working_cat
DBSession_working_cat = sessionmaker(bind=engine_working_cat)
db_session = DBSession_working_cat()

def save(user):
    db_session = DBSession_working_cat()
    user_to_add = User()
    user_to_add.id = str(user.id)

    user_to_add._level = user.level
    user_to_add._experience = user._experience
    user_to_add.until_level = user.until_level
    user_to_add.experience_coef_level = user.experience_coef_level
    user_to_add.coins = user.coins + 150

    user_to_add.username = user.username
    user_to_add.fullname = user.fullname
    user_to_add.chat_id = user.chat_id
    if user.cat_name == '':
        user_to_add.cat_name = 'Неизвестный кот'
    else:    
        user_to_add.cat_name = user.cat_name
    user_to_add.status = 'idle'

    user_to_add.current_work = None
    user_to_add.is_working = False
    user_to_add.current_treasure_hunt = None
    user_to_add.is_treasure_hunting = False

    user_to_add.gems = user.gems

    user_to_add.toy_mouse_acquired = user.toy_mouse_acquired
    user_to_add.toy_bow_acquired = user.toy_bow_acquired
    user_to_add.toy_ball_acquired = user.toy_ball_acquired
    user_to_add._experience_multiplier = user._experience_multiplier

    user_to_add.food_fish_acquired = user.food_fish_acquired
    user_to_add.food_premium_acquired = user.food_premium_acquired
    user_to_add.food_shrimp_acquired = user.food_shrimp_acquired
    user_to_add._speed_multiplier = user._speed_multiplier

    user_to_add.home_small_acquired = user.home_small_acquired
    user_to_add.home_flat_acquired = user.home_flat_acquired
    user_to_add.home_house_acquired = user.home_house_acquired
    user_to_add.home_mansion_acquired = user.home_mansion_acquired
    user_to_add._coins_multiplier = user._coins_multiplier

    user_to_add.experience_donated = user.experience_donated
    user_to_add.coins_donated = user.coins_donated
    user_to_add.trophies = pickle.dumps(user.trophies)

    db_session.add(user_to_add)
    db_session.commit()
    db_session.close()

def save_cat_committee(cat_committee):
    db_session = DBSession_working_cat()
    cat_committee_to_add = CatCommittee()
    cat_committee_to_add.id = str('cat_committee')

    cat_committee_to_add._level = cat_committee.level
    cat_committee_to_add._experience = cat_committee._experience
    cat_committee_to_add.until_level = cat_committee.until_level
    cat_committee_to_add.experience_coef_level = cat_committee.experience_coef_level
    cat_committee_to_add.coins = cat_committee.coins

    db_session.add(cat_committee_to_add)
    db_session.commit()
    db_session.close()

db = SqliteDict(sqlite_users)
for user_key in db:
    try:
        save(db[user_key])
    except Exception as e:
        print(e)

db = SqliteDict(sqlite_cat_committee)
for user_key in db:
    try:
        save_cat_committee(db[user_key])
    except Exception as e:
        print(e)