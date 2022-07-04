import shelve
from config import shelve_users

class User(object):

    def __init__(self, id='', username='', fullname='', chat_id=0, cat_name='', status='new'):
        self.id = id
        self.username = username
        self.fullname = fullname
        self.chat_id = chat_id
        self.cat_name = cat_name
        self.status = status
        
        self.current_work = None
        self._level = 1
        self._experience = 0
        self._until_level = 10
        self.coins = 0

        self.work_timer_dict = {'wash_dish': 15, 'vacuum': 15, 'bake': 15, 'tiktok': 15,
                                'advertisement': 15}
        self.work_experience_dict = {'wash_dish': 5, 'vacuum': 7, 'bake': 10, 'tiktok': 14,
                                     'advertisement': 19}
        self.work_coins_dict = {'wash_dish': 5, 'vacuum': 7, 'bake': 10, 'tiktok': 14,
                                'advertisement': 19}
        

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
        if self._experience >= self._until_level:
            self.level_up()

    @property
    def until_level(self):
        return self._until_level

    @until_level.setter
    def until_level(self, until_level):
        self._until_level = until_level

    def save(self):
        """Saves user class instance"""
        with shelve.open(shelve_users) as users:
            users[self.id] = self

    def level_up(self):
        self.experience = self.experience - self.level * 10
        self.level += 1
        self.until_level = self.level * 10