telegram_token = 'Your telegram bot token'

log_file = 'bot.log'

sqlite_users = 'data/users.sqlite'
sqlite_timers = 'data/timers.sqlite'
sqlite_cat_committee = 'data/cat_committee.sqlite'

db_login     = 'user'
db_password  = 'password'
db_name      = 'working_cat'
server_name  = 'localhost'
charset      = 'utf8mb4'
conn_string  = 'mysql://{0}:{1}@{2}/{3}?charset={4}'.format(db_login, db_password, server_name, db_name, charset)