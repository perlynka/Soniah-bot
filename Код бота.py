import telebot
from telebot import types
import math
import random
from datetime import datetime
import os
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot('6088950763:AAHFX03Zi6RGDokyLJDrbb3mISoNSA6Nrow')


@bot.message_handler(commands = ['start'])

def start(message):
    topics_kb = types.InlineKeyboardMarkup(row_width = 1)
    physics_btn = types.InlineKeyboardButton(text = 'Фізика', callback_data = 'topic1')
    maths_btn = types.InlineKeyboardButton(text = 'Математика', callback_data = 'topic2')
    geography_btn = types.InlineKeyboardButton(text = 'Географія', callback_data = 'topic3')
    astronomy_btn = types.InlineKeyboardButton(text = 'Аcтрономія', callback_data = 'topic4')
    common_btn = types.InlineKeyboardButton(text = 'Загальні запитання', callback_data = 'topic5')
    topics_kb.add(physics_btn, maths_btn, geography_btn, astronomy_btn, common_btn)
    greeting = f'''Привіт, <i>{message.from_user.first_name}</i>! Мене звати <b>Сонях🌻</b>. Я - бот, що відповідає на твої запитання. Обери тему, яка тобі потрібна❤️'''

    greeting_mess = bot.send_message(message.chat.id, greeting, reply_markup = topics_kb, parse_mode='html')
    time.sleep(10)
    bot.delete_message(message.chat.id, greeting_mess.id)

@bot.callback_query_handler(func = lambda callback: True)
def check_callback_topics(callback):
    if callback.data == 'topic1':
        physics_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        physics_btn_1 = types.KeyboardButton(text = 'Обчислення потужності за законом Стефана-Больцмана')
        physics_btn_2 = types.KeyboardButton(text = 'Виведення сталої Планка')
        physics_kb.add(physics_btn_1, physics_btn_2)
        bot.send_message(callback.message.chat.id, ''' «Дайте мені точку опори - і я переверну світ», - сказав якось Архімед, маючи на увазі важіль. 

Я, на жаль, не допоможу із задачками про важелі, але можу запропонувати цілих два запитання із <b>фізики❄🔥</b> Яке тебе цікавить?''', reply_markup = physics_kb, parse_mode='html')
    elif callback.data == 'topic2':
        maths_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        maths_btn_1 = types.KeyboardButton(text = 'Обчислення квадратного рівняння')
        maths_btn_2 = types.KeyboardButton(text = 'Обчислення скалярного добутку векторів')
        maths_btn_3 = types.KeyboardButton(text = 'Обчислення відстані від точки до прямої в просторі')
        maths_btn_4 = types.KeyboardButton(text = 'Обчислення площі трикутника')
        maths_btn_5 = types.KeyboardButton(text = 'Виведення н-го числа Фібоначчі')
        maths_btn_6 = types.KeyboardButton(text = 'Виведення числа π')
        maths_kb.add(maths_btn_1, maths_btn_2, maths_btn_3, maths_btn_4, maths_btn_5, maths_btn_6)
        bot.send_message(callback.message.chat.id, '<b>Математика?📊📐</b>Співчуваю😔 В цій темі є шість питань. Вибери, яке тебе цікавить😊', reply_markup = maths_kb, parse_mode='html')
    elif callback.data == 'topic3':
        geography_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        geography_btn_1 = types.KeyboardButton(text = '5 найвищих гір світу')
        geography_btn_2 = types.KeyboardButton(text = 'Дві держави, що мають найбільшу кількість кордонів з іншими державами')
        geography_btn_3 = types.KeyboardButton(text = 'Найбільш населене місто світу')
        geography_btn_4 = types.KeyboardButton(text = 'Дві держави, які мають найбільшу кількість водосховищ в світі')
        geography_kb.add(geography_btn_1, geography_btn_2, geography_btn_3, geography_btn_4)
        bot.send_message(callback.message.chat.id, 'Любиш подорожувати? <b>Географія🗺🧭</b> - прекрасний вибір! В цій темі я маю чотири запитання. Що тебе цікавить?', reply_markup = geography_kb, parse_mode='html')
    elif callback.data == 'topic4':
        astronomy_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        astronomy_btn_1 = types.KeyboardButton(text = 'Відстань між Землею та Сонцем')
        astronomy_btn_2 = types.KeyboardButton(text = 'Що таке астероїди та комети')
        astronomy_btn_3 = types.KeyboardButton(text = 'Процеси, що відбуваються на Сонці, та їхній вплив на Землю')
        astronomy_kb.add(astronomy_btn_1, astronomy_btn_2, astronomy_btn_3)
        bot.send_message(callback.message.chat.id, '''«Дві речі наповнюють душу завжди новим і дедалі сильнішим подивом [...] — це зоряне небо наді мною і моральний закон у мені», - писав Іммануїл Кант. 
                         
Що ж, <b>астрономія</b> - вкрай захоплива тема!🚀🪐 У ній я маю три запитання. Що тебе цікавить?😉''', reply_markup = astronomy_kb, parse_mode='html')    
    elif callback.data == 'topic5':
        common_kb = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
        common_btn_1 = types.KeyboardButton(text = 'Який зараз рік?')
        common_btn_2 = types.KeyboardButton(text = 'Скільки днів у ___ році')
        common_btn_3 = types.KeyboardButton(text = 'Зіграймо у вгадай число між 1 та 10')
        common_btn_4 = types.KeyboardButton(text = 'Заспівай улюблену пісню')
        common_btn_5 = types.KeyboardButton(text = 'Розкажи анекдот!')
        common_btn_6 = types.KeyboardButton(text = 'Топ-5 найбагатших людей світу')
        common_btn_7 = types.KeyboardButton(text = 'Що було раніше: курка чи яйце?')
        common_btn_8 = types.KeyboardButton(text = 'Що подивитись ввечері?')
        common_btn_9 = types.KeyboardButton(text = 'Під яку музику позайматись спортом?')
        common_btn_10 = types.KeyboardButton(text = 'Як життя, сонях?')
        common_kb.add(common_btn_1, common_btn_2, common_btn_3, common_btn_4, common_btn_5, common_btn_6, common_btn_7, common_btn_8, common_btn_9, common_btn_10)
        bot.send_message(callback.message.chat.id, '<b>Загальні запитання</b> - найцікавіша з усіх тем.🥳🥳 В цій темі є десять питань. Якt тобі до вподоби?😉', reply_markup = common_kb, parse_mode='html')

@bot.message_handler()
def questions(message):
    if message.text == 'Обчислення потужності за законом Стефана-Больцмана':
        a = types.ReplyKeyboardRemove()
        msg_physics = bot.send_message(message.chat.id, f'''Обрана тобою тема - <b>Обчислення потужності за законом Стефана-Больцмана</b>. Введи площу поверхні тіла в м^2 та абсолютну температуру тіла в К без одиниць вимірювання через пробіл🤗''', reply_markup = a, parse_mode='html')
        bot.register_next_step_handler(msg_physics, func_stefan_boltzmann_law)
    elif message.text == 'Виведення сталої Планка':
       a = types.ReplyKeyboardRemove()
       bot.send_message(message.chat.id, '''Фундаментальна фізична <b>стала Планка</b> позначається літерою ℎ і в Системі інтернаціональній її визначено так:

<b>h = 6.62607015×10^−34 Дж⋅с (Дж = кг⋅м^2 ⋅ с^−2)</b>''', reply_markup = a, parse_mode = 'html')
    elif message.text == 'Обчислення квадратного рівняння':
        a = types.ReplyKeyboardRemove()
        msg_quadratic_equation = bot.send_message(message.chat.id, '<b>Квадратне рівняння?</b> Ізі!😎 Напиши значення параметрів а, b і c без ком через пробіл', reply_markup = a, parse_mode='html')
        bot.register_next_step_handler(msg_quadratic_equation, func_quadratic_equation)
    elif message.text == 'Обчислення скалярного добутку векторів':
        a = types.ReplyKeyboardRemove()
        msg_dot_product = bot.send_message(message.chat.id, '<b>Скалярний добуток?</b> Та запросто!😁 Напиши мені значення координат а та b і кута θ між ними без ком через пробіл і я все швидко порахую!', reply_markup = a, parse_mode='html')
        bot.register_next_step_handler(msg_dot_product, func_dot_product)
    elif message.text == 'Обчислення відстані від точки до прямої в просторі':
        a = types.ReplyKeyboardRemove()
        msg_distance = bot.send_message(message.chat.id, '<b>Відстань від точки до прямої в просторі...</b> Гм, не таке вже й легке запитання🤔 Напиши мені координати точки в просторі і координати точок а та b на цій прямій через пробіл без дужок і ком. Спробую щось придумати', reply_markup = a, parse_mode='html')
        bot.register_next_step_handler(msg_distance, func_distance)
    elif message.text == 'Обчислення площі трикутника':
        a = types.ReplyKeyboardRemove()
        msg_triangle = bot.send_message(message.chat.id, '<b>Площа трикутника?</b> Це мені до снаги!🤟 Напиши довжину основи трикутника і довжину висоти, опущеної на цю основу, без пробілів, ком та одиниць вимірювання, і я скажу тобі площу твого трикутника🤗', reply_markup = a, parse_mode='html')
        bot.register_next_step_handler(msg_triangle, func_triangle)
    elif message.text == 'Виведення н-го числа Фібоначчі':
        a = types.ReplyKeyboardRemove()
        msg_fibonacci = bot.send_message(message.chat.id, '<b>Числа Фібоначчі?</b> Ну і запитання у тебе звісно... Ух, буде складно, але я спробую це зробити. Введи своє число н', reply_markup = a, parse_mode='html')
        bot.register_next_step_handler(msg_fibonacci, func_fibonacci)        
    elif message.text == 'Виведення числа π':
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Число π (пі) для програмування та використання при складних і точних обчисленнях комп‘ютером — <b>3,14159265358979.</b>', reply_markup = a, parse_mode='html')
    elif message.text == '5 найвищих гір світу':
        a = types.ReplyKeyboardRemove()
        bot.send_photo(message.chat.id, 'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcRh6kEzhH9PktdhztbPzjD6ohLYRKJZx0rQ3PRYFfWMbu-FG4WSm79ntCS7_U20tPkK', reply_markup = a)
        bot.send_message(message.chat.id, '''<b>Топ-5 найвищих гір світу</b>

<b>5. Макалу.</b>
Ця гора, як і майже всі решта гір у топі, знаходиться в Гімалаях. Висота - <b>8463 м.</b>

<b>4. Лхоцзе.</b>
Ця гора містить три вершини: Лхоцзе Головну, Лхоцзе Середню і Лхоцзе Шар. Цікавий факт: середній пік гори Лхоцзе, за даними Книги рекордів Гінесса на 2008 р., — найвища серед непідкорених вершин. Висота цієї гори складає <b>8516 м.</b>

<b>3. Канченджанґа</b>
Назва «Канченджанґа» означає «п'ять снігових скарбів». Висота цієї гори - <b>8586 м</b> над рівнем моря.

<b>2.Чоґорі</b>
Чоґорі - єдина гора з цього топу, яка знаходиться не в Гімалаях, а в іншому гірському масиві, який називається Каракорум. Висота гори - <b>8611 м.</b>

<b>1. Еверест</b>
Інша назва цієї гори - Джомолунгма - з тибетської означає 'Мати Всесвіту'. Висота Евересту - <b>8848 м.</b>
        ''', parse_mode='html')
    elif message.text == 'Дві держави, що мають найбільшу кількість кордонів з іншими державами':
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '''Найбільшу кількість країн-сусідок мають <b>Китай та Росія.</b> 

Китай межує з 14 державами. Сусідніми державами Китаю є: Монголія, Росія, Казахстан, Киргизстан, Таджикистан, Афганістан, Пакистан, Індія, Непал, Північна Корея, Бутан, М'янма, Лаос та В'єтнам.

Росія також має 14 сусідів. Сусідніми державами Росії є: Китай, Україна, Білорусь, Польща, Північна Корея, Казахстан, Фінляндія, Грузія, Норвегія, Монголія, Литва, Азербайджан, Естонія та Латвія.''', reply_markup = a, parse_mode='html')
    elif message.text == 'Найбільш населене місто світу':
        a = types.ReplyKeyboardRemove()
        bot.send_photo(message.chat.id, 'https://planetofhotels.com/guide/sites/default/files/styles/big_gallery_image/public/text_gallery/Shanghai-3.jpg', reply_markup = a)
        bot.send_message(message.chat.id, 'Найбільш густо населеним у світі є місто <b>Шанхай</b>, що знаходиться у Китаї. Кількість населення складає 24,150,000', parse_mode='html')
    elif message.text == 'Дві держави, які мають найбільшу кількість водосховищ в світі':
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, ''' Державами з найбільшою кількістю водосховищ є <b>Бразилія та Росія.</b> 

1. Бразилія

Запаси прісної води – 6 950 куб. км

На душу населення – 43,0 тис. куб. м

2. Росія

Запаси прісної води – 4500 куб. км

На душу населення – 30,5 тис. куб. м''', reply_markup = a, parse_mode='html')
    elif message.text == 'Відстань між Землею та Сонцем':
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '''Середня відстань від Землі до Сонця становить приблизно <b>149,6 млн. км.</b> Більш точне число - 149 597 870 700 м, воно також називається астрономічною одиницею.''', reply_markup = a, parse_mode='html')
    elif message.text == 'Що таке астероїди та комети':
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '''<b>Астероїд</b> — невелике небесне тіло розміром від метрів до сотень кілометрів, яке обертається кеплерівською орбітою навколо Сонця.

<b>Комета</b> - мале тіло Сонячної системи, яке обертається навколо Сонця і має так звану кому та/або хвіст.''', reply_markup = a, parse_mode='html')    
    elif message.text == 'Процеси, що відбуваються на Сонці, та їхній вплив на Землю':
        a = types.ReplyKeyboardRemove()
        bot.send_photo(message.chat.id, 'https://4.bp.blogspot.com/-NOhm0yRSVRc/UOluz84WIYI/AAAAAAAAEEc/Cuvk7WEEZkA/s1600/%D1%81%D0%BE%D0%BD%D1%86%D0%B5+%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%B5.bmp', reply_markup = a)
        bot.send_message(message.chat.id, '''Сонячну активність ділять на два види: сонячні плями та сонячні цикли. 
Сонячні плями — це порівняно темні області на фотосфері Сонця, в яких інтенсивне магнітне поле знижує температуру плазми на 2000 K.

Сонячними циклами називають періодичні зміни сонячної активності. Один такий цикл триває 11 років. 

<b>Вплив сонячної активності на клімат:</b>
У ритмі з циклами сонячної активності настають певні коливання клімату Землі. У тисячолітньому циклі істотно коливається рівень води в озерах і морях. 

<b>Вплив сонячної активності на рослинність:</b>
Було проведено дослідження на річних кільцях секвої, і воно виявило, що роки максимумів сонячної активності приріст дерев був більшим, ніж у роки мінімумів. Також врожайність сільськогосподарських культур співвідноситься з кількістю сонячних плям.

<b>Вплив сонячної активності на тварин:</b>
До тваринного світу належать бактерії та віруси, що спричиняють різноманітні захворювання у людей і тварин. Під час зміни сонячної активності змінюється чисельність бактерій та вірусів, які спричиняють різноманітні захворювання. Це впливає на поширення епідемій і пандемій, а також на поширення масових захворювань тварин. У роки високої сонячної активності виникають пандемії холери, грипу, дизентерії, дифтерії тощо.

<b>Влив сонячної активності на людей:</b>
У людей з хворобами серцево-судинної системи під час геомагнітних бур, спричинених Сонцем, погіршується стан, збільшується число інфарктів та інсультів. У здорових людей змінюється сприйняття часу, сповільнюється рухова реакція, знижується короткочасна пам'ять, об'єм та інтенсивність уваги. Навіть у спеціально тренованих людей - спортсменів вищого класу та льотчиків — зафіксовано підвищену кількість помилок при виконанні контрольних завдань.
 ''', parse_mode='html')
    elif message.text == 'Який зараз рік?':
        a = types.ReplyKeyboardRemove()
        mess_time = message.date
        mess_year = datetime.utcfromtimestamp(mess_time).strftime('%Y')
        bot.send_message(message.chat.id, f'Зараз <b>{mess_year} рік</b>', reply_markup = a, parse_mode='html')
    elif message.text == 'Скільки днів у ___ році':
        a = types.ReplyKeyboardRemove()
        msg_days_in_year = bot.send_message(message.chat.id, 'Введи рік числом без слів', reply_markup = a)
        bot.register_next_step_handler(msg_days_in_year, func_days_in_year)
    elif message.text == 'Заспівай улюблену пісню':
        a = types.ReplyKeyboardRemove()
        song_path = os.path.join(os.getcwd(), 'D:\Библиотека (.docx)\улюблені пісні', random.choice(os.listdir('D:\Библиотека (.docx)\улюблені пісні')))
        bot.send_audio(message.chat.id, open(song_path, 'rb'), reply_markup = a)
    elif message.text == 'Зіграймо у вгадай число між 1 та 10':
        a = types.ReplyKeyboardRemove()
        msg_game = bot.send_message(message.chat.id, 'Введи твоє число', reply_markup = a,)
        bot.register_next_step_handler(msg_game, func_game)
    elif message.text == 'Розкажи анекдот!':
        a = types.ReplyKeyboardRemove()
        jokes = ['''Штірліц готувався до бою...
        


        

...а прийшла ґьорл''', '''Операційна. Медсестра кричить:
– У нього з’явився пульс, він повертається!
Тут лікар вирубає електрику:
– Повертатися – погана прикмета.''', 'Штірліц довго дивився на одну крапку. Потім перевів погляд на иншу крапку. “Двокрапка” — здогадався Штірліц.', 'Штирліц сидів дома. З вікна дуло. Штирліц натиснув Alt+F4 — вікно зникло.', 'Вечорами Мальвіна любила дивитися одним оком на зоряне небо та згадувати той незабутній поцілунок Буратіно.']
        bot.send_message(message.chat.id, random.choice(jokes), reply_markup = a,)
    elif message.text == 'Топ-5 найбагатших людей світу':
        a = types.ReplyKeyboardRemove()
        bot.send_photo(message.chat.id, 'https://img.freepik.com/premium-vector/rich-wealthy-happy-smiling-businessman-worker-entrepreneur-character-sitting-pile_133260-2079.jpg', reply_markup = a)
        bot.send_message(message.chat.id, '''<b>1. Бернар Арно</b>
<b>Власний капітал:</b> $210,8 млрд

<b>Джерело статків:</b> LVMH/товари розкоші

<b>Вік:</b> 73

<b>Громадянство:</b> Франція

Бернар Арно – гендиректор і голова LVMH, найбільшої компанії розкішних товарі у світі, яка володіє 70 модними і косметичними брендами. Серед найвідоміших Louis Vuitton, Christian Dior, Moet & Chandon і Sephora. У 2021-му LVMH також викупила ювелірний бренд Tiffany & Co. за $15,8 млрд.

<b>2. Ілон Маск</b>
<b>Власний капітал:</b> $196,5 млрд

<b>Джерело статків:</b> Tesla, SpaceX, Twitter

<b>Вік:</b> 51 рік

<b>Громадянство:</b> США

Маск – гендиректор електромобільної компанії Tesla, космічної фірми SpaceX і соцмережі Twitter. Він володіє приблизно 21% акцій і опціонів Tesla, але більше половини з них під заставою кредитів. Електромобільна компанія «відповідає» за дві треті статків Маска. У жовтні 2022-го він купив Twitter за $44 млрд і тримає близько 74% компанії.

<b>3. Джефф Безос</b>
<b>Власний капітал:</b> $117,4 млрд

<b>Джерело статків:</b> Amazon

<b>Вік:</b> 59

<b>Громадянство:</b> США

У липні 2021-го Джефф Безос пішов із посади гендиректора Amazon, але залишається її головою; того ж місяця він полетів у космос на приватній ракеті, яку збудувала його компанія Blue Origin.

<b>4. Ларрі Еллісон</b>
<b>Власний капітал:</b> $112,3 млрд

<b>Джерело статків:</b> Oracle

<b>Вік:</b> 78

<b>Громадянство:</b> США

Ларрі Еллісон став співзасновником компанії програмного забезпечення Oracle у 1977-му і був її гендиректором до 2014-го; тепер він займає посаду голови компанії і головного технологічного директора. За роки біля керма Oracle він зробив низку великих придбань, серед яких Sun Microsystems у 2010-му.

<b>5. Воррен Баффетт</b>
<b>Власний капітал:</b> $106,4 млрд

<b>Джерело статків:</b> Berkshire Hathaway

<b>Вік:</b> 92

<b>Громадянство:</b> США

Відомий як «Оракул з Омахи», Воррен Баффетт є одним із найуспішніших інвесторів усіх часів. Він управляє інвестиційним конгломератом Berkshire Hathaway, до якого входять десятки компаній, серед яких страховик Geico, виробник батарейок Duracell і мережа ресторанів Dairy Queen. Син американського конгресмена, він уперше купив акції в 11 років, а в 13 уперше подав податкову декларацію.''', parse_mode='html')
    elif message.text == 'Що було раніше: курка чи яйце?':
        a = types.ReplyKeyboardRemove()
        bot.send_photo(message.chat.id, 'https://img.tsn.ua/cached/115/tsn-d7721072f5f1787fa1f16a6df613a75f/thumbs/1036x648/b6/5a/423e19327435eaeb23b71f8a12905ab6.jpeg',  reply_markup = a)
        bot.send_message(message.chat.id, '''Біологи впевнені, якщо говорити про яйця як такі, то вони точно з'явилися раніше. Але, коли йдеться саме про домашніх курей, тут справа вже інакша. В такому разі першою була курка, в якої потім з'явилося яйце. Здається, що таке неможливо, але вчені пояснили свою позицію.

За словами Коена Стейна з Королівського бельгійського інституту природничих наук, яйця в шкаралупі, які відкладали стародавні тварини стали найважливішою стадією еволюції. Завдяки тому, що вони почали відкладати яйця на суші, вони змогли поступово віддалитися від води та розпочати свою власну історію.

Говорячи про птахів загалом, до яких також належать кури, вченими були виявлені їхні перші скам'янілі рештки, яким від 165 до 150 мільйонів років. Однак, за нещодавними дослідженнями виявляється — перші яйця в твердій шкаралупі з'явилися аж 325 мільйонів років тому.

Тобто, як стверджує Стейн, яйця все ж з'явилися раніше за "курку" як птаха. Однак перші яйця мали м'яку оболонку і були більше схожі на ті, які відкладають сьогодні качконоси чи рептилії. 

Однак, якщо говорити саме про домашню курку, а не просто птахів, тоді справа набирає іншого оберту. 2021 року вченими було з'ясовано, що звичайні кури, яких розводять по всьому світі, походять від джунглевих (вони мешкали в джунглях Південно-Східної Азії). Приблизно 50 мільйонів років тому вони відокремилися від своїх предків і спочатку не були домашніми. Проте між 1650 до н.е. і 1250 до н.е. люди змогли їх приручити.

В певний момент під час процесу одомашнення сучасних курей їхній останній предок відклав яйце, в якому був ембріон із достатньою кількістю генетичних відмінностей, щоб повністю відрізнятися від вигляду батьків. Цей ембріон розвивався ще не в яйці звичайної курки. І лише тоді, коли він перетворився на дорослого птаха, з'явилося нове потомство, яке і стало справжніми предками домашніх курей. Тому, можна сказати, що спочатку була курка, яка вже потім знесла яйце.

<i>[інформація з сайту ТСН]</i>
''', parse_mode='html')
    elif message.text == 'Що подивитись ввечері?':
        movies = ['''<b>«Мій пес ідіот»
Рік виходу</b> – 2020
<b>Рейтинг IMDb</b> – 6,2

У кожного хоч раз у житті наступала криза, коли все йде шкереберть. Так і в письменника Анрі сталось. Чоловік не може написати заплановану книгу через брак натхнення. А тут ще й у сім'ї негаразди, адже Анрі не може знайти спільну мову з дружиною та винить у всьому своїх дорослих дітей. І коли, здавалось би, гірше бути не може, у житті головного героя з'являється безпритульний собака, який може кардинально змінити будні письменника. 

Глядачі побачать не тільки курйозні пригоди Анрі у фільмі «Мій пес ідіот», але й особливу дружбу, що є між твариною та людиною.
''', '''<b>«Дівчина мого найкращого друга»
Рік виходу</b> – 2008
<b>Рейтинг IMDb</b> – 5,9

Якщо ви маєте настрій переглянути романтичну комедію, тоді «Дівчина мого найкращого друга» може стати чудовим вибором.

За сюжетом, красень Танк має незвичну роботу. Його наймають покинуті хлопці, які прагнуть повернути своїх коханих. А працює все просто: після жахливого побачення з Танком дівчата переосмислюють попередні стосунки та думають, що вони не були вже такими й поганими. І в цій справі головний герой просто професіонал, поки в його житті не з'являється Алексіс. То що ж обрати Танку: кохання чи допомогу найкращому другу?
''', '''<b>«Віолет і Дейзі»
Рік виходу</b> – 2012
<b>Рейтинг IMDb</b> – 6,1

Якщо ваші друзі не в захваті від типових американських комедій, запропонуйте фільм «Віолет і Дейзі». Цей комедійний бойовик сподобається любителям екшну, адже головні героїні – професійні найманки, які беруться за складну справу та при відмові можуть самі стати мішенями кілерів. Окрім цього, дівчата змушені будуть зробити переоцінку своєї роботи та загалом життя.
''', '''<b>«Астерікс на Олімпійських іграх»
Рік виходу</b> – 2008
<b>Рейтинг IMDb</b> – 5,2

Мабуть, не знайдеться любителя мультфільмів, який би не знав, хто такі Астерікс та Обелікс. Після шаленого успіху анімаційних стрічок в Європі відзняли серію фільмів про цих персонажів. Один з них – «Астерікс на Олімпійських іграх».

За сюжетом франшизи, Галлія опинилась у складі Римської імперії. І тільки одне невеличке село з легкістю чинить опір озброєним воїнам та самому Юлію Цезарю з його загарбницькими стратегіями. А секрет їхній у зіллі, яке надає навіть наймолодшим галлам суперсилу. У стрічці «Астерікс на Олімпійських іграх» головні герої допомагатимуть односельцю Полюбвіксу, який взаємно закоханий у принцесу. Дівчина має вийти заміж за сина Цезаря, а щоб відтягнути цей момент, обіцяє піти до вівтаря з переможцем знаменитих змагань. Тому романтичні пригоди у поєднанні з гумором глядачам гарантовані.''', '''<b>«Похмілля у Вегасі»
Рік виходу</b> – 2009
<b>Рейтинг IMDb</b> – 7,7

Якщо ви хотіли б 2 години реготати з чудової комедії, кращого фільму для перегляду з друзями, аніж «Похмілля у Вегасі», не знайти. Тут є все: шалені пригоди, курйозні ситуації, романтична лінія та сюжет, який неможливо передбачити до кінця. А що може статись з чоловіками, які приїхали розважитись у Лас-Вегас – побачите у чудовій комедії.
''']
        fav_movie = random.choice(movies)
        if 'Мій пес' in fav_movie: 
            a = types.ReplyKeyboardRemove()
            bot.send_photo(message.chat.id, 'https://planetakino.ua/res/get-poster/00000000000000000000000000002505/1600-1040_MyStupidDog.jpg',  reply_markup = a)
            bot.send_message(message.chat.id, f' {fav_movie} [Інформацію взято з сайту 24tv.ua]', parse_mode='html')
        elif 'Дівчина мого найкращого друга' in fav_movie:
            a = types.ReplyKeyboardRemove()
            bot.send_photo(message.chat.id, 'https://m.media-amazon.com/images/I/51YSoCnhxgL.jpg', reply_markup = a)
            bot.send_message(message.chat.id, f' {fav_movie} [Інформацію взято з сайту 24tv.ua]', parse_mode='html')
        elif 'Віолет і Дейзі' in fav_movie:
            a = types.ReplyKeyboardRemove()
            bot.send_photo(message.chat.id, 'https://www.film.ru/sites/default/files/styles/epsa_685x385/public/trailers_frame/f_110988.jpg', reply_markup = a) 
            bot.send_message(message.chat.id, f' {fav_movie} [Інформацію взято з сайту 24tv.ua]', parse_mode='html')
        elif 'Астерікс на Олімпійських іграх' in fav_movie:
            a = types.ReplyKeyboardRemove()
            bot.send_photo(message.chat.id, 'https://s6.vcdn.biz/static/f/1414570551/image.jpg/pt/r300x423x4',  reply_markup = a) 
            bot.send_message(message.chat.id, f' {fav_movie} [Інформацію взято з сайту 24tv.ua]', parse_mode='html')
        else:
            a = types.ReplyKeyboardRemove()
            bot.send_photo(message.chat.id, 'https://ictv.ua/wp-content/uploads/2016/12/16/Pohmillya-u-Vegasi-1.jpg',  reply_markup = a) 
            bot.send_message(message.chat.id, f' {fav_movie} [Інформацію взято з сайту 24tv.ua]', parse_mode='html')
    elif message.text == 'Під яку музику позайматись спортом?':
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '''Спеціально для тебе я підготував підбадьорливий плейлист для тренування!❤️‍🔥 Тримай посилання💋
 
https://open.spotify.com/playlist/0PbxEjdlNqanHSSy4AeEdJ?si=304c113d112144bb                        ''',  reply_markup = a)
    elif message.text == 'Як життя, сонях?':
        mental_illness = ['Я загубився у просторі і часі. Я не відчуваю бажання щось робити, я хочу тільки лежати, дивитися в стелю, слухати шмаркливі плейлисти з ютубу і рюмсати. Я не знаю, хто я і що роблю в цьому світі.', 'Все супер! Мої дітки-соняшки ходять до хорошої школи, у мене турботлива дружина і дружна сім‘я, як можна не радіти життю?🥰', 'Кляте сонце знову зайшло за горизонт надто рано і тепер я вимушений цілу ніч витріщатись у сиру землю таке відчуття ніби бог нас десь наказує за шось🫠🫠', 'У мене все чудово! Я дістав баночку малинового варення і збираюсь пити чай😊 Приєднуйся! Я завжди тобі радий)']
        rand_illnes = random.choice(mental_illness)
        if 'Я загубився у просторі і часі' in rand_illnes:
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, rand_illnes, reply_markup = a)
            video = open('D:\Библиотека (.docx)\Навчання\Бот\Сонях журбинка.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        elif 'Кляте сонце знову зайшло' in rand_illnes:
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, rand_illnes, reply_markup = a)
            bot.send_photo(message.chat.id, 'https://i.pinimg.com/564x/4e/f5/2f/4ef52f211a2e8522ffb204bc5927c030.jpg')
        elif 'Все супер' in rand_illnes:
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, rand_illnes,  reply_markup = a)
            bot.send_photo(message.chat.id, 'https://i.pinimg.com/564x/85/7a/1f/857a1ff3da794fa55382e26090252ee9.jpg')
        else:
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, rand_illnes,  reply_markup = a)
            bot.send_photo(message.chat.id, 'https://i.pinimg.com/564x/23/ee/e8/23eee8da6d90050f05c306971e17ac79.jpg')
    elif message.text == '/help':
        bot.send_message(message.chat.id, )
            
    else:
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Я не знаю такої теми😢 Спробуй ще раз', reply_markup=a)


def func_stefan_boltzmann_law(message):
    a, t = message.text.split()
    A = int(a)
    T = int(t)
    P = 5.67 * A * T**4
    bot.send_message(message.chat.id, f'Потужність випромінювання: <b>Р = {P}</b>', parse_mode='html')
    
def func_quadratic_equation(message):
    A, B, C = message.text.split()
    a = float(A)
    b = float(B)
    c = float(C)
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        bot.send_message(message.chat.id, f'''x1 = {x1}
x2 = {x2}''')
    elif d == 0:
        x = -b / (2 * a) 
        bot.send_message(message.chat.id, f'x = {x}')
    else:
        bot.send_message(message.chat.id, 'Рівняння не має коренів')

def func_dot_product(message):
    A, B, C = message.text.split()
    a = int(A)
    b = int(B)
    c = int(C)
    dot_pr = abs(a) * abs(b) * c
    bot.send_message(message.chat.id, f'Скалярний добуток даних векторів - {dot_pr}')

def func_distance(message):
    P, A, B = message.text.split()
    p = int(P)
    a = int(A)
    b = int(B)
    distance = (abs(p - a) * abs(p - b))/abs(b-a)
    bot.send_message(message.chat.id, f'Все вийшло! Відстань від точки до прямої дорівнює {distance}!')

def func_triangle(message):
    B, H = message.text.split()
    b = int(B)
    h = int(H)
    triangle = 0.5 * b * h
    bot.send_message(message.chat.id, f'Площа твого трикутника - {triangle}')

def func_fibonacci(message):
    n = int(message.text)
    f_1 = 1
    f_2 = 1
    bot.send_message(message.chat.id, f'{f_1}')
    while f_2 < n:
        bot.send_message(message.chat.id, f'{f_2}')
        f_1, f_2 = f_2, f_1 + f_2


def func_days_in_year(message):
    year = int(message.text)
    year_nums = list(message.text)
    if len(year_nums) > 4:
        bot.send_message(message.chat.id, 'Йой! Здається, рік введений неправильно(( Чи ти - прибулець із майбутнього?😁')    
    elif year%4 == 0:
        bot.send_message(message.chat.id, 'Це - високосний рік, у ньому 366 днів.')
    else:
        bot.send_message(message.chat.id, 'Це - невисокосний рік. У ньому 365 днів.')

def func_game(message):
    target = random.randint(0, 10) 
    guess = int(message.text) 
    if target == guess:
        bot.send_message(message.chat.id, 'Перемога!🥳🥳')
    else:
        bot.send_message(message.chat.id, f'Я загадав число {target}, але твоїм числом було {guess}😖')
        time.sleep(3)
        end_game = ['Це було весело! Давай пограємо ще наступного разу🥰', 'Чудово зіграли) Сподіваюсь, тобі теж було весело❤️', 'Це була крута гра! Шкода, що час вже сплинув😥']
        bot.send_message(message.chat.id, random.choice(end_game))

bot.polling(non_stop=True)

 

