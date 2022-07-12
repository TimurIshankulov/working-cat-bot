SYMBOL_CAT = '🐈'
SYMBOL_LEVEL = '🔼'
SYMBOL_STATUS = '💬'
SYMBOL_EXPERIENCE = '🏆'
SYMBOL_COINS = '💰'
SYMBOL_GEMS = '💎'
SYMBOL_BONUS = '🏅'
SYMBOL_ATTENTION = '❗'
SYMBOL_QUESTION = '❓'
SYMBOL_CHECK = '✅'

SYMBOL_WORK = '💼'
SUMBOL_IDLE = '💤'

SYMBOL_WASH_DISH = '🍽'
SYMBOL_VACUUM = '🧹'
SYMBOL_BAKE = '🥧'
SYMBOL_TIKTOK = '🎥'
SYMBOL_ADVERTISEMENT = '🎬'

SYMBOL_TOYS = '🧶'
SYMBOL_MOUSE = '🐭'
SYMBOL_BOW = '🎀'
SYMBOL_BALL = '⚽'

SYMBOL_FOOD = '🍣'
SYMBOL_FISH = '🎣'
SYMBOL_PREMIUM = '🍲'
SYMBOL_SHRIMP = '🦐'

SYMBOL_HOME = '🏡'
SYMBOL_SMALL = '🏠'
SYMBOL_FLAT = '🏠'
SYMBOL_HOUSE = '🏠'

SYMBOL_TREASURE = '🗝'
SYMBOL_SOLO = '🪙'
SYMBOL_EXPEDITION = '📜'

SYMBOL_RATING = '🥇'


REPLY_UNKNOWN_STATUS = 'Внутренняя ошибка статуса пользователя'

GREETING_1 = 'Приветствую тебя! Назови имя своего ' + SYMBOL_CAT + ' ленивого кота, который не хочет работать:'
GREETING_2 = 'Имя твоего ' + SYMBOL_CAT + ' питомца: {0}.\n\
Добро пожаловать в игру "Работящий кот". Вы можете отправлять своего кота на ' + \
SYMBOL_WORK + ' работу, покупать для него ' + SYMBOL_TOYS + ' игрушки, ' + \
SYMBOL_FOOD + ' корм и ' + SYMBOL_HOME + ' дома, чтобы получить дополнительные ' + SYMBOL_BONUS + \
' бонусы.\nЦель игры — приобрести ' + SYMBOL_HOUSE + ' особняк, чтобы твой ' + SYMBOL_CAT + \
' котик ни в чем себе не отказывал!\n' + SYMBOL_ATTENTION + 'Примечание. Некоторые возможности \
открываются только с ростом ' + SYMBOL_LEVEL + ' уровня ' + SYMBOL_CAT + ' котика.'

STATUS_OVERALL = SYMBOL_CAT + ' Кот {0}\n' + \
SYMBOL_LEVEL + ' Уровень: {1}\n' + \
SYMBOL_STATUS + ' Статус: {2}\n' + \
SYMBOL_EXPERIENCE + ' Опыт: {3:.1f}/{4}\n' + \
SYMBOL_COINS + ' Монеты: {5:.1f}\n' + \
SYMBOL_GEMS + ' Самоцветы: {6}'

CAT_STATUS_IDLE = SUMBOL_IDLE + ' отдыхает'
CAT_STATUS_ON_WORK = SYMBOL_WORK + ' работает'
CAT_STATUS_ON_TREASURE_HUNT = SYMBOL_TREASURE + ' ищет сокровища'
CAT_STATUS_WAITING = 'ожидает указаний'

BACK_TO_MAIN_MENU = 'Возврат в основное меню.'
MENU_STATUS = 'Статус'
MENU_WORK = 'Работа'
MENU_TOYS = 'Игрушки'
MENU_FOOD = 'Корм'
MENU_HOME = 'Дома'
MENU_TREASURE_HUNT = 'Поиск сокровищ'
MENU_TROPHIES = 'Трофеи'
MENU_BACK = 'Назад'
MENU_CAT_COMMITTEE = 'Котовский комитет'
MENU_CAT_COMMITTEE_STATUS = 'Статус комитета'
MENU_CAT_COMMITTEE_DONATE = 'Пожертвовать монеты'
MENU_CAT_COMMITTEE_BACK = 'Назад'
MENU_CAT_COMMITTEE_RATING = 'Рейтинг'
MENU_CAT_COMMITTEE_TO_MENU = 'Возврат в меню Котовского комитета.'

WORK_CHOOSE_WORK = 'Выберите ' + SYMBOL_WORK + ' работу для своего кота. Чем сложнее работа, тем больше она вознаграждается!'
WORK_STRING_WORKING = SYMBOL_WORK + ' Работаем...\n'
WORK_WASH_DISH_STARTED = '{0} приступил к ' + SYMBOL_WASH_DISH + ' мытью посуды. Помогаем кожаным мешкам!'
WORK_WASH_DISH_DESC = SYMBOL_WASH_DISH + ' Мыть посуду ({0} мин.)'
WORK_VACUUM_STARTED = '{0} начал ' + SYMBOL_VACUUM + ' пылесосить квартиру. Чистота в доме важна для кошаков!'
WORK_VACUUM_DESC = SYMBOL_VACUUM + ' Пропылесосить ({0} мин.)'
WORK_BAKE_STARTED = '{0} приступил к ' + SYMBOL_BAKE + ' выпеканию шарлотки. Скоро будет очень вкусно!'
WORK_BAKE_DESC = SYMBOL_BAKE + ' Выпекать шарлотку ({0} мин.)'
WORK_TIKTOK_STARTED = '{0} начал ' + SYMBOL_TIKTOK + ' снимать трендовые тик-токи. Не беспокоить!'
WORK_TIKTOK_DESC = SYMBOL_TIKTOK + ' Снимать тик-токи ({0} мин.)'
WORK_ADVERTISEMENT_STARTED = '{0} ' + SYMBOL_ADVERTISEMENT + ' снимается в рекламе кошачьего корма. Свет, камера, мотор!'
WORK_ADVERTISEMENT_DESC = SYMBOL_ADVERTISEMENT + ' Реклама кошачьего корма ({0} мин.)'
WORK_KIND_DICT = {'wash_dish': WORK_WASH_DISH_STARTED,
                  'vacuum': WORK_VACUUM_STARTED,
                  'bake': WORK_BAKE_STARTED,
                  'tiktok': WORK_TIKTOK_STARTED,
                  'advertisement': WORK_ADVERTISEMENT_STARTED}
WORK_ALREADY_WORKING = '{0} уже работает, за сверхурочные ему не заплатят!'
WORK_DONE = SYMBOL_WORK + ' {0} завершил свою работу.\n' + SYMBOL_EXPERIENCE + ' Получено очков \
опыта: {1:.1f}\n' + SYMBOL_COINS + ' Получено монет: {2}'

TOYS_CHOOSE_TOY = 'Выберите ' + SYMBOL_TOYS + ' игрушку для своего кота. Чем дороже игрушка, тем больше бонус к получаемому опыту!'
TOYS_MOUSE_ACQUIRED = 'Поздравляем! Вы приобрели ' + SYMBOL_MOUSE + ' игрушечную мышь для кота и получили постоянный бонус + 10% к получаемому опыту!'
TOYS_MOUSE_DESC = SYMBOL_MOUSE + ' Мышка (' + SYMBOL_COINS + ' 100)'
TOYS_BOW_ACQUIRED = 'Поздравляем! Вы приобрели ' + SYMBOL_BOW + ' бантик на веревке и получили постоянный бонус + 20% к получаемому опыту!'
TOYS_BOW_DESC = SYMBOL_BOW + ' Бантик на веревке (' + SYMBOL_COINS + ' 200)'
TOYS_BALL_ACQUIRED = 'Поздравляем! Вы приобрели ' + SYMBOL_BALL + ' шарик для игры и получили постоянный бонус + 30% к получаемому опыту!'
TOYS_BALL_DESC = SYMBOL_BALL + ' Шарик-погремушка (' + SYMBOL_COINS + ' 300)'
TOYS_KIND_DICT = {'toy_mouse': TOYS_MOUSE_ACQUIRED,
                  'toy_bow': TOYS_BOW_ACQUIRED,
                  'toy_ball': TOYS_BALL_ACQUIRED}
TOYS_ALREADY_ACQUIRED = SYMBOL_TOYS + ' Игрушка уже приобретена!'
TOYS_INSUFFICIENT_COINS = SYMBOL_COINS + ' Недостаточно монет для покупки!'

FOOD_CHOOSE_FOOD = 'Выберите ' + SYMBOL_FOOD + ' корм для своего кота. Чем дороже корм, тем больше бонус к скорости выполнения заданий!'
FOOD_FISH_ACQUIRED = 'Поздравляем! Вы покормили своего кота ' + SYMBOL_FISH + \
' рыбкой и получили постоянный бонус + 10% к скорости выполнения заданий!'
FOOD_FISH_DESC = SYMBOL_FISH + ' Рыбка (' + SYMBOL_COINS + ' 100)'
FOOD_PREMIUM_ACQUIRED = 'Поздравляем! Вы покормили своего кота ' + SYMBOL_PREMIUM + \
' премиум-кормом и получили постоянный бонус + 20% к скорости выполнения заданий!'
FOOD_PREMIUM_DESC = SYMBOL_PREMIUM + ' Премиум-корм (' + SYMBOL_COINS + ' 200)'
FOOD_SHRIMP_ACQUIRED = 'Поздравляем! Вы покормили своего кота ' + SYMBOL_SHRIMP + \
' королевской креветкой и получили постоянный бонус + 30% к скорости выполнения заданий!'
FOOD_SHRIMP_DESC = SYMBOL_SHRIMP + ' Королевская креветка (' + SYMBOL_COINS + ' 300 )'
FOOD_KIND_DICT = {'food_fish': FOOD_FISH_ACQUIRED,
                  'food_premium': FOOD_PREMIUM_ACQUIRED,
                  'food_shrimp': FOOD_SHRIMP_ACQUIRED}
FOOD_ALREADY_ACQUIRED = SYMBOL_FOOD + ' Вы уже кормили кота этим кормом!'
FOOD_INSUFFICIENT_COINS = SYMBOL_COINS + ' Недостаточно монет для покупки!'

HOME_CHOOSE_HOME = 'Выберите ' + SYMBOL_SMALL + ' дом для своего кота. Чем дороже дом, тем больше бонус к получаемым монетам!'
HOME_SMALL_ACQUIRED = 'Поздравляем! Вы приобрели ' + SYMBOL_SMALL + ' скромный кошачий домик и получили постоянный бонус + 30% к получаемым монетам!'
HOME_SMALL_DESC = SYMBOL_SMALL + ' Кошачий домик (' + SYMBOL_COINS + ' {0}, ' + SYMBOL_GEMS + ' {1})'
HOME_FLAT_ACQUIRED = 'Поздравляем! Вы приобрели ' + SYMBOL_FLAT + ' целую квартиру и получили постоянный бонус + 60% к получаемым монетам!'
HOME_FLAT_DESC = SYMBOL_FLAT + ' Своя квартира (' + SYMBOL_COINS + ' {0}, ' + SYMBOL_GEMS + ' {1})'
HOME_HOUSE_ACQUIRED = 'Поздравляем! Вы приобрели ' + SYMBOL_HOUSE + ' двухэтажный коттедж и получили постоянный бонус + 100% к получаемым монетам!'
HOME_HOUSE_DESC = SYMBOL_HOUSE + ' Двухэтажный коттедж (' + SYMBOL_COINS + ' {0}, ' + SYMBOL_GEMS + ' {1})'
HOME_KIND_DICT = {'home_small': HOME_SMALL_ACQUIRED,
                  'home_flat': HOME_FLAT_ACQUIRED,
                  'home_house': HOME_HOUSE_ACQUIRED}
HOME_ALREADY_ACQUIRED = SYMBOL_HOME + ' Вы уже приобрели этот дом!'
HOME_INSUFFICIENT_COINS = SYMBOL_COINS + ' Недостаточно монет для покупки!'
HOME_INSUFFICIENT_GEMS = SYMBOL_GEMS + ' Недостаточно самоцветов для покупки!'
HOME_LOW_LEVEL = SYMBOL_ATTENTION + 'Покупка домов доступна с 5 уровня!'

TREASURE_HUNT_CHOOSE_TREASURE_HUNT = 'Выберите одну из доступных активностей по ' + SYMBOL_TREASURE + \
' поиску сокровищ! Награды увеличиваются для более сложных поисков.'
TREASURE_HUNT_STRING_HUNTING = SYMBOL_TREASURE + ' Ищем сокровища...\n'
TREASURE_HUNT_SOLO_STARTED = '{0} приступил к ' + SYMBOL_SOLO + ' поиску сокровищ в одиночку, используя металлодетектор! Постараемся найти хоть что-то ценное...'
TREASURE_HUNT_SOLO_DESC = SYMBOL_SOLO + ' Поиск с металлодетектором (60 мин.)'
TREASURE_HUNT_TREASURE_STARTED = '{0} со своим другом воспользуется картой сокровищ, чтобы найти и \
откопать ' + SYMBOL_TREASURE + ' зарытый пиратами клад! Успехов с добычей!'
TREASURE_HUNT_TREASURE_DESC = SYMBOL_TREASURE + ' Искать клад с другом (90 мин.)'
TREASURE_HUNT_EXPEDITION_STARTED = '{0} ' + SYMBOL_EXPEDITION + ' снарядил экспедицию, чтобы найти древние сокровища забытых наций!'
TREASURE_HUNT_EXPEDITION_DESC = SYMBOL_EXPEDITION + ' Снарядить экспедицию (120 мин.)'
TREASURE_HUNT_KIND_DICT = {'solo': TREASURE_HUNT_SOLO_STARTED,
                           'treasure': TREASURE_HUNT_TREASURE_STARTED,
                           'expedition': TREASURE_HUNT_EXPEDITION_STARTED}
TREASURE_HUNT_LOW_LEVEL = SYMBOL_ATTENTION + 'Эта активность доступна только с 5 уровня!'
TREASURE_HUNT_ALREADY_HUNTING = '{0} уже ищет сокровища, не разорваться же!'
TREASURE_HUNT_DONE = SYMBOL_TREASURE + '{0} завершил поиск сокровищ.\n' + \
SYMBOL_COINS + ' Получено монет: {1:.1f}\n' + \
SYMBOL_GEMS + ' Получено самоцветов: {2}'
TREASURE_HUNT_FAILED = SYMBOL_TREASURE + ' Поиски сокровищ не увенчались успехом :( . Повезет в следующий раз!'

TROPHY_A_NAME = SYMBOL_CHECK + ' Шерстяной клубочек'
TROPHY_B_NAME = SYMBOL_CHECK + ' Когтеточка с мятой'
TROPHY_C_NAME = SYMBOL_CHECK + ' Флакончик валерианы'
TROPHY_D_NAME = SYMBOL_CHECK + ' Миска с бесконечным кормом'
TROPHY_E_NAME = SYMBOL_CHECK + ' Мышка на батарейках'
TROPHY_F_NAME = SYMBOL_CHECK + ' Кошачья трава'
TROPHY_G_NAME = SYMBOL_CHECK + ' Фурминатор'
TROPHY_H_NAME = SYMBOL_CHECK + ' Робот-пылесос'
TROPHY_I_NAME = SYMBOL_CHECK + ' Мини-фонтан'
TROPHY_J_NAME = SYMBOL_CHECK + ' Всегда чистый лоточек'
TROPHY_UNKNOWN = SYMBOL_QUESTION + ' Неизвестный трофей'
TROPHIES_DICT = {'a': TROPHY_A_NAME,
                 'b': TROPHY_B_NAME,
                 'c': TROPHY_C_NAME,
                 'd': TROPHY_D_NAME,
                 'e': TROPHY_E_NAME,
                 'f': TROPHY_F_NAME,
                 'g': TROPHY_G_NAME,
                 'h': TROPHY_H_NAME,
                 'i': TROPHY_I_NAME,
                 'j': TROPHY_J_NAME}
TROPHY_AQUIRED = 'Поздравляем! Вы получили редкий трофей: {0}!'

CAT_COMMITTEE_GREETING = 'Добро пожаловать в Котовский комитет!\n\
Это особое учреждение, которое получает ' + SYMBOL_EXPERIENCE + ' опыт от работы всех котов,\
а также принимает ' + SYMBOL_COINS + ' пожертвования на различные цели. Здесь можно ознакомиться с' + \
SYMBOL_RATING + ' рейтингом котов по количеству пожертвованных монет комитету.'
CAT_COMMITTEE_STATUS = SYMBOL_CAT + ' Котовский комитет\n' + \
SYMBOL_LEVEL + ' Уровень: {0}\n' + \
SYMBOL_EXPERIENCE + ' Опыт: {1:.1f}/{2}\n' + \
SYMBOL_COINS + ' Казна: {3:.1f}'
CAT_COMMITTEE_CHOOSE_DONATE = 'Выберите сумму для пожертвования.'
CAT_COMMITTEE_DONATE_TEA = 'На чай с печеньками  (' + SYMBOL_COINS + ' 50)'
CAT_COMMITTEE_DONATE_PAPER = 'Бумага для принтера  (' + SYMBOL_COINS + ' 100)'
CAT_COMMITTEE_DONATE_RENOVATION = 'Капитальный ремонт (' + SYMBOL_COINS + ' 200)'
CAT_COMMITTEE_DONATE_SUCCESSFUL = SYMBOL_COINS + ' Вы успешно пожертвовали Котовскому комитету {0} монет.'
CAT_COMMITTEE_INSUFFICIENT_COINS = SYMBOL_COINS + ' Недостаточно монет для пожертвования!'
CAT_COMMITTEE_ERROR_OCCURRED = 'Произошла ошибка пожертвования монет.'