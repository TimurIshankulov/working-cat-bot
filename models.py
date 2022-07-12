from sqlitedict import SqliteDict
from config import sqlite_users, sqlite_cat_committee

class Base():
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


class User(Base):
    def __init__(self, id='', username='', fullname='', chat_id=0, cat_name='', status='new'):
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
        self._coins_multiplier = 1

        self.experience_donated = 0
        self.coins_donated = 0

        self.trophies = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False,
                         'f': False, 'g': False, 'h': False, 'i': False, 'j': False}

    def __str__(self):
        return ('ID: {self.id}, \
                 Username: {self.username}, \
                 Fullname: {self.fullname}, \
                 Chat ID: {self.chat_id}, \
                 Status: {self.status}'.format(self=self))

    @property
    def log_str(self):
        """Returns log string"""
        return '{self.fullname} <{self.username}>'.format(self=self)

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

    def save(self):
        """Saves user class instance"""
        db = SqliteDict(sqlite_users)
        db[self.id] = self
        db.commit()
        db.close()


class CatCommittee(Base):
    def __init__(self) -> None:
        Base.__init__(self)
        self.until_level = 100
        self.experience_coef_level = 100

    def save(self):
        db = SqliteDict(sqlite_cat_committee)
        db['cat_committee'] = self
        db.commit()
        db.close()
