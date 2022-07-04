REPLY_UNKNOWN_STATUS = 'Внутренняя ошибка статуса пользователя'

GREETING_1 = 'Приветствую тебя! Назови имя своего ленивого кота, который не хочет работать:'
GREETING_2 = 'Имя твоего питомца: {0}'

STATUS_OVERALL = 'Кот {0}.\nСтатус: {1}\nУровень: {2}\nОпыт: {3}/{4}\nМонеты: {5}'

CAT_STATUS_IDLE = 'отдыхает'
CAT_STATUS_ON_WORK = 'работает'

CHOOSE_WORK = 'Выберите работу для своего кота.'
WORK_WASH_DISH_STARTED = '{0} приступил к мытью посуды. Помогаем кожаным мешкам.'
WORK_WASH_DISH_DESC = 'Мыть посуду ({0} мин., {1} ед. опыта)'
WORK_VACUUM_STARTED = '{0} начал пылесосить квартиру. Чистота в квартире важна для кошаков!'
WORK_VACUUM_DESC = 'Пропылесосить ({0} мин., {1} ед. опыта)'
WORK_BAKE_STARTED = '{0} приступил к выпеканию шарлотки. Скоро будет очень вкусно!'
WORK_BAKE_DESC = 'Выпекать шарлотку ({0} мин., {1} ед. опыта)'
WORK_TIKTOK_STARTED = '{0} начал снимать трендовые тик-токи. Не беспокоить!'
WORK_TIKTOK_DESC = 'Снимать тик-токи ({0} мин., {1} ед. опыта)'
WORK_ADVERTISEMENT_STARTED = '{0} снимается в рекламе кошачьего корма. Свет, камера, мотор!'
WORK_ADVERTISEMENT_DESC = 'Реклама кошачьего корма ({0} мин., {1} ед. опыта)'
WORK_BACK_TO_MAIN_MENU = 'Возврат в основное меню.'
WORK_KIND_DICT = {'wash_dish': WORK_WASH_DISH_STARTED,
                  'vacuum': WORK_VACUUM_STARTED,
                  'bake': WORK_BAKE_STARTED,
                  'tiktok': WORK_TIKTOK_STARTED,
                  'advertisement': WORK_ADVERTISEMENT_STARTED}
WORK_DONE = '{0} завершил свою работу и получил {1} очков опыта.'
