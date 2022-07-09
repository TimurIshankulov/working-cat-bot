REPLY_UNKNOWN_STATUS = 'Внутренняя ошибка статуса пользователя'

GREETING_1 = 'Приветствую тебя! Назови имя своего ленивого кота, который не хочет работать:'
GREETING_2 = 'Имя твоего питомца: {0}.\n\
Добро пожаловать в игру "Работящий кот". Вы можете отправлять своего кота на работу,\
покупать для него игрушки, корм и дома, чтобы получить дополнительные бонусы.\n\
Цель игры — приобрести двухэтажный коттедж, чтобы твой котик ни в чем себе не отказывал!\n\
Примечание. Некоторые возможности открываются только с ростом уровня котика.'

STATUS_OVERALL = 'Кот {0}\nУровень: {1}\nСтатус: {2}\nОпыт: {3:.1f}/{4}\nМонеты: {5:.1f}\nСамоцветы: {6}'

CAT_STATUS_IDLE = 'отдыхает'
CAT_STATUS_ON_WORK = 'работает'
CAT_STATUS_WAITING = 'ожидает указаний'

BACK_TO_MAIN_MENU = 'Возврат в основное меню.'
MENU_STATUS = 'Статус'
MENU_WORK = 'Работа'
MENU_TOYS = 'Игрушки'
MENU_FOOD = 'Корм'
MENU_HOME = 'Дома'
MENU_TREASURE_HUNT = 'Поиск сокровищ'
MENU_BACK = 'Назад'

WORK_CHOOSE_WORK = 'Выберите работу для своего кота. Чем сложнее работа, тем больше она вознаграждается!'
WORK_STRING_WORKING = 'Работаем...\n'
WORK_WASH_DISH_STARTED = '{0} приступил к мытью посуды. Помогаем кожаным мешкам!'
WORK_WASH_DISH_DESC = 'Мыть посуду ({0} мин.)'
WORK_VACUUM_STARTED = '{0} начал пылесосить квартиру. Чистота в доме важна для кошаков!'
WORK_VACUUM_DESC = 'Пропылесосить ({0} мин.)'
WORK_BAKE_STARTED = '{0} приступил к выпеканию шарлотки. Скоро будет очень вкусно!'
WORK_BAKE_DESC = 'Выпекать шарлотку ({0} мин.)'
WORK_TIKTOK_STARTED = '{0} начал снимать трендовые тик-токи. Не беспокоить!'
WORK_TIKTOK_DESC = 'Снимать тик-токи ({0} мин.)'
WORK_ADVERTISEMENT_STARTED = '{0} снимается в рекламе кошачьего корма. Свет, камера, мотор!'
WORK_ADVERTISEMENT_DESC = 'Реклама кошачьего корма ({0} мин.)'
WORK_KIND_DICT = {'wash_dish': WORK_WASH_DISH_STARTED,
                  'vacuum': WORK_VACUUM_STARTED,
                  'bake': WORK_BAKE_STARTED,
                  'tiktok': WORK_TIKTOK_STARTED,
                  'advertisement': WORK_ADVERTISEMENT_STARTED}
WORK_ALREADY_WORKING = '{0} уже работает, за сверхурочные ему не заплатят!'
WORK_DONE = '{0} завершил свою работу.\nПолучено очков опыта: {1:.1f}\nПолучено монет: {2}'

TOYS_CHOOSE_TOY = 'Выберите игрушку для своего кота. Чем дороже игрушка, тем больше бонус к получаемому опыту!'
TOYS_MOUSE_ACQUIRED = 'Поздравляем! Вы приобрели игрушечную мышь для кота и получили постоянный бонус + 10% к получаемому опыту!'
TOYS_MOUSE_DESC = 'Мышка (100 монет)'
TOYS_BOW_ACQUIRED = 'Поздравляем! Вы приобрели бантик на веревке и получили постоянный бонус + 20% к получаемому опыту!'
TOYS_BOW_DESC = 'Бантик на веревке (200 монет)'
TOYS_BALL_ACQUIRED = 'Поздравляем! Вы приобрели шарик для игры и получили постоянный бонус + 30% к получаемому опыту!'
TOYS_BALL_DESC = 'Шарик-погремушка (300 монет)'
TOYS_KIND_DICT = {'toy_mouse': TOYS_MOUSE_ACQUIRED,
                  'toy_bow': TOYS_BOW_ACQUIRED,
                  'toy_ball': TOYS_BALL_ACQUIRED}
TOYS_ALREADY_ACQUIRED = 'Игрушка уже приобретена!'
TOYS_INSUFFICIENT_COINS = 'Недостаточно монет для покупки!'

FOOD_CHOOSE_FOOD = 'Выберите корм для своего кота. Чем дороже корм, тем больше бонус к скорости выполнения заданий!'
FOOD_FISH_ACQUIRED = 'Поздравляем! Вы покормили своего кота рыбкой и получили постоянный бонус + 10% к скорости выполнения заданий!'
FOOD_FISH_DESC = 'Рыбка (100 монет)'
FOOD_PREMIUM_ACQUIRED = 'Поздравляем! Вы покормили своего кота премиум-кормом и получили постоянный бонус + 20% к скорости выполнения заданий!'
FOOD_PREMIUM_DESC = 'Премиум-корм (200 монет)'
FOOD_SHRIMP_ACQUIRED = 'Поздравляем! Вы покормили своего кота королевской креветкой и получили постоянный бонус + 30% к скорости выполнения заданий!'
FOOD_SHRIMP_DESC = 'Королевская креветка (300 монет)'
FOOD_KIND_DICT = {'food_fish': FOOD_FISH_ACQUIRED,
                  'food_premium': FOOD_PREMIUM_ACQUIRED,
                  'food_shrimp': FOOD_SHRIMP_ACQUIRED}
FOOD_ALREADY_ACQUIRED = 'Вы уже кормили кота этим кормом!'
FOOD_INSUFFICIENT_COINS = 'Недостаточно монет для покупки!'

HOME_CHOOSE_HOME = 'Выберите дом для своего кота. Чем дороже дом, тем больше бонус к получаемым монетам!'
HOME_SMALL_ACQUIRED = 'Поздравляем! Вы приобрели скромный кошачий домик и получили постоянный бонус + 30% к получаемым за работу монетам!'
HOME_SMALL_DESC = 'Скромный кошачий домик (300 монет)'
HOME_FLAT_ACQUIRED = 'Поздравляем! Вы приобрели целую квартиру и получили постоянный бонус + 60% к получаемым за работу монетам!'
HOME_FLAT_DESC = 'Своя квартира (600 монет)'
HOME_HOUSE_ACQUIRED = 'Поздравляем! Вы приобрели двухэтажный коттедж и получили постоянный бонус + 100% к получаемым за работу монетам!'
HOME_HOUSE_DESC = 'Двухэтажный коттедж (1000 монет)'
HOME_KIND_DICT = {'home_small': HOME_SMALL_ACQUIRED,
                  'home_flat': HOME_FLAT_ACQUIRED,
                  'home_house': HOME_HOUSE_ACQUIRED}
HOME_ALREADY_ACQUIRED = 'Вы уже приобрели этот дом!'
HOME_INSUFFICIENT_COINS = 'Недостаточно монет для покупки!'
HOME_LOW_LEVEL = 'Покупка домов доступна с 5 уровня!'

TREASURE_HUNT_LOW_LEVEL = 'Эта активность доступна только с 5 уровня!'
TREASURE_HUNT_CHOOSE_TREASURE_HUNT = 'Выберите одну из доступных активностей по поиску сокровищ! Награды увеличиваются для более сложных поисков.'
TREASURE_HUNT_STRING_HUNTING = 'Ищем сокровища...\n'
TREASURE_HUNT_SOLO_STARTED = '{0} приступил к поиску сокровищ в одиночку, используя металлодетектор! Постараемся найти хоть что-то ценное...'
TREASURE_HUNT_SOLO_DESC = 'Поиск с металлодетектором (60 мин.)'
TREASURE_HUNT_TREASURE_STARTED = '{0} со своим другом воспользуется картой сокровищ, чтобы найти и откопать зарытый пиратами клад! Успехов с добычей!'
TREASURE_HUNT_TREASURE_DESC = 'Искать клад с другом (100 мин.)'
TREASURE_HUNT_EXPEDITION_STARTED = '{0} снарядил экспедицию, чтобы найти древние сокровища забытых наций!'
TREASURE_HUNT_EXPEDITION_DESC = 'Снарядить экспедицию (150 мин.)'
TREASURE_HUNT_KIND_DICT = {'solo': TREASURE_HUNT_SOLO_STARTED,
                           'treasure': TREASURE_HUNT_TREASURE_STARTED,
                           'expedition': TREASURE_HUNT_EXPEDITION_STARTED}
TREASURE_HUNT_ALREADY_HUNTING = '{0} уже ищет сокровища, не разорваться же!'
TREASURE_HUNT_DONE = '{0} завершил поиск сокровищ.\nПолучено монет: {1:.1f}\nПолучено самоцветов: {2}'
TREASURE_HUNT_FAILED = 'Поиски сокровищ не увенчались успехом :( . Повезет в следующий раз!'