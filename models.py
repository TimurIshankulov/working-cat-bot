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

    def save(self):
        """Saves user class instance"""
        with shelve.open(shelve_users) as users:
            users[self.id] = self

    