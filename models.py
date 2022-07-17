import pickle
import sys

from sqlalchemy import Column, Integer, String, BLOB, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from icecream import ic

from config import conn_string

DeclarativeBase = declarative_base()
engine_working_cat = create_engine(conn_string)
DBSession_working_cat = sessionmaker(bind=engine_working_cat)
#db_session = DBSession_working_cat()

class Base(DeclarativeBase):
    def __init__(self) -> None:
        self._level = 1
        self._experience = 0.0
        self.until_level = 10
        self.experience_coef_level = 10
        self.coins = 0.0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        self._experience = experience
        if self._experience >= self.until_level:
            self.level_up()

    def level_up(self):
        while self._experience >= self.until_level:
            self._experience = self._experience - self.level * self.experience_coef_level
            self.level += 1
            self.until_level = self.level * self.experience_coef_level

    #====== Table options ======#

    __tablename__ = 'users'

    id = Column(String(20), primary_key=True, nullable=False)

    _level = Column(Integer())
    _experience = Column(Float())
    until_level = Column(Integer())
    experience_coef_level = Column(Integer)
    coins = Column(Float())


class User(Base):
    def __init__(self, id='', username='', fullname='', chat_id=0, cat_name='Неизвестный кот',
                 status='new'):
        Base.__init__(self)
        self.experience_coef_level = 10

        self.id = id
        self.username = username
        self.fullname = fullname
        self.chat_id = chat_id
        self.cat_name = cat_name
        self.status = status
        
        self.current_work = None
        self.is_working = False
        self.current_treasure_hunt = None
        self.is_treasure_hunting = False

        self.gems = 0

        self.toy_mouse_acquired = False
        self.toy_bow_acquired = False
        self.toy_ball_acquired = False
        self._experience_multiplier = 1

        self.food_fish_acquired = False
        self.food_premium_acquired = False
        self.food_shrimp_acquired = False
        self._speed_multiplier = 1

        self.home_small_acquired = False
        self.home_flat_acquired = False
        self.home_house_acquired = False
        self.home_mansion_acquired = False
        self._coins_multiplier = 1

        self.experience_donated = 0
        self.coins_donated = 0

        self.trophies = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False,
                         'f': False, 'g': False, 'h': False, 'i': False, 'j': False}

    #====== Table options ======#

    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    username = Column(String(50))
    fullname = Column(String(60))
    chat_id = Column(String(20))
    cat_name = Column(String(50))
    status = Column(String(50))

    current_work = Column(String(50))
    is_working = Column(Boolean())
    current_treasure_hunt = Column(String(50))
    is_treasure_hunting = Column(Boolean())

    gems = Column(Integer())

    toy_mouse_acquired = Column(Boolean())
    toy_bow_acquired = Column(Boolean())
    toy_ball_acquired = Column(Boolean())
    _experience_multiplier = Column(Float())

    food_fish_acquired = Column(Boolean())
    food_premium_acquired = Column(Boolean())
    food_shrimp_acquired = Column(Boolean())
    _speed_multiplier = Column(Float())

    home_small_acquired = Column(Boolean())
    home_flat_acquired = Column(Boolean())
    home_house_acquired = Column(Boolean())
    home_mansion_acquired = Column(Boolean())
    _coins_multiplier = Column(Float())

    experience_donated = Column(Float())
    coins_donated = Column(Integer())
    trophies = Column(BLOB())

    #====== Overrided Methods ======#

    def __str__(self):
        return (f'ID: {self.id}, ' + \
                f'Username: {self.username}, ' + \
                f'Fullname: {self.fullname}, ' + \
                f'Chat ID: {self.chat_id}, ' + \
                f'Status: {self.status}, ' + \
                f'Is working: {self.is_working}, ' + \
                f'Is treasure hunting: {self.is_treasure_hunting}')

    #====== Properties ======#

    @property
    def experience_multiplier(self):
        additional_coef = 0
        if self.toy_mouse_acquired:
            additional_coef += 0.1
        if self.toy_bow_acquired:
            additional_coef += 0.2
        if self.toy_ball_acquired:
            additional_coef += 0.3
        return self._experience_multiplier + additional_coef

    @experience_multiplier.setter
    def experience_multiplier(self, experience_multiplier):
        self._experience_multiplier = experience_multiplier

    @property
    def speed_multiplier(self):
        additional_coef = 0
        if self.food_fish_acquired:
            additional_coef += 0.1
        if self.food_premium_acquired:
            additional_coef += 0.2
        if self.food_shrimp_acquired:
            additional_coef += 0.3
        return self._speed_multiplier - additional_coef

    @experience_multiplier.setter
    def experience_multiplier(self, experience_multiplier):
        self._coins_multiplier = experience_multiplier

    @property
    def coins_multiplier(self):
        additional_coef = 0
        if self.home_small_acquired:
            additional_coef += 0.3
        if self.home_flat_acquired:
            additional_coef += 0.6
        if self.home_house_acquired:
            additional_coef += 1.0
        return self._coins_multiplier + additional_coef

    @coins_multiplier.setter
    def coins_multiplier(self, coins_multiplier):
        self._coins_multiplier = coins_multiplier

    #====== Methods ======#

    def save(self):
        user_was_none = False
        db_session = DBSession_working_cat()
        user = db_session.query(User).filter_by(id=self.id).first()
        if user is None:
            user = self
            user_was_none = True
        
        user._level = self.level
        user._experience = self._experience
        user.until_level = self.until_level
        user.experience_coef_level = self.experience_coef_level
        user.coins = self.coins

        user.id = self.id
        user.username = self.username
        user.fullname = self.fullname
        user.chat_id = self.chat_id
        user.cat_name = self.cat_name
        user.status = self.status

        user.current_work = self.current_work
        user.is_working = self.is_working
        user.current_treasure_hunt = self.current_treasure_hunt
        user.is_treasure_hunting = self.is_treasure_hunting

        user.gems = self.gems

        user.toy_mouse_acquired = self.toy_mouse_acquired
        user.toy_bow_acquired = self.toy_bow_acquired
        user.toy_ball_acquired = self.toy_ball_acquired
        user._experience_multiplier = self._experience_multiplier

        user.food_fish_acquired = self.food_fish_acquired
        user.food_premium_acquired = self.food_premium_acquired
        user.food_shrimp_acquired = self.food_shrimp_acquired
        user._speed_multiplier = self._speed_multiplier

        user.home_small_acquired = self.home_small_acquired
        user.home_flat_acquired = self.home_flat_acquired
        user.home_house_acquired = self.home_house_acquired
        user.home_mansion_acquired = self.home_mansion_acquired
        user._coins_multiplier = self._coins_multiplier

        user.experience_donated = self.experience_donated
        user.coins_donated = self.coins_donated
        user.trophies = pickle.dumps(self.trophies)

        if user_was_none:
            db_session.add(user)
            
        try:
            db_session.commit()
        except Exception:
            print(sys.exc_info()[1])
            db_session.rollback()
        finally:
            db_session.close()


class CatCommittee(DeclarativeBase):
    def __init__(self) -> None:
        self._level = 1
        self._experience = 0.0
        self.until_level = 100
        self.experience_coef_level = 100
        self.coins = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        self._experience = experience
        if self._experience >= self.until_level:
            self.level_up()

    def level_up(self):
        while self._experience >= self.until_level:
            self._experience = self._experience - self.level * self.experience_coef_level
            self.level += 1
            self.until_level = self.level * self.experience_coef_level

    #====== Table options ======#

    __tablename__ = 'cat_committee'

    id = Column(String(20), primary_key=True, nullable=False)

    _level = Column(Integer())
    _experience = Column(Float())
    until_level = Column(Integer())
    experience_coef_level = Column(Integer)
    coins = Column(Float())

    #====== Methods ======#

    def save(self):
        cat_committee_was_none = False
        db_session = DBSession_working_cat()

        cat_committee = db_session.query(CatCommittee).filter_by(id='cat_committee').first()
        if cat_committee is None:
            cat_committee = self
            cat_committee_was_none = True
        cat_committee._level = self._level
        cat_committee._experience = self._experience
        cat_committee.until_level = self.until_level
        cat_committee.experience_coef_level = self.experience_coef_level
        cat_committee.coins = self.coins

        if cat_committee_was_none:
            cat_committee.id = 'cat_committee'
            db_session.add(cat_committee)
        try:
            db_session.commit()
        except Exception:
            db_session.rollback()
        finally:
            db_session.close()

class Timer(DeclarativeBase):
    def __init__(self, id=None, user=None, chat_id=None, message_id=None, message_text=None,
                 start_timestamp=None, seconds=None, timer_type=None):
        self.id = id
        self.user = user
        self.chat_id = chat_id
        self.message_id = message_id
        self.message_text = message_text
        self.start_timestamp = start_timestamp
        self.seconds = seconds
        self.timer_type = timer_type

    #====== Table options ======#

    __tablename__ = 'timers'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    user = Column(BLOB())
    chat_id = Column(String(20))
    message_id = Column(Integer())
    message_text = Column(String(400))
    start_timestamp = Column(Integer())
    seconds = Column(Integer())
    timer_type = Column(String(50))

    #====== Methods ======#

    def save(self):
        timer_was_none = False
        db_session = DBSession_working_cat()

        timer = db_session.query(Timer).filter_by(id=self.id).first()
        if timer is None:
            timer = self
            timer_was_none = True
        else:
            self.user = pickle.loads(self.user)

        timer.user = pickle.dumps(self.user)
        timer.chat_id = self.chat_id
        timer.message_id = self.message_id
        timer.message_text = self.message_text
        timer.start_timestamp = self.start_timestamp
        timer.seconds = self.seconds
        timer.timer_type = self.timer_type

        if timer_was_none:
            db_session.add(timer)
        try:
            db_session.commit()
            db_session.refresh(timer)
            self.id = timer.id
        except Exception:
            db_session.rollback()
        finally:
            db_session.close()
        

DeclarativeBase.metadata.create_all(engine_working_cat)
DeclarativeBase.metadata.bind = engine_working_cat