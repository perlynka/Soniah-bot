# Як розширити список тем і завдань для бота "Сонях". Інструкція

Розгляньмо алгоритм роширення списку тем і завдання на наочному прикладі. Нехай ми хочемо додати тему _Література_, яка має два завдання _Назвати відомих шістдесятників_ та _Цікаві факти про Івана Франка_.

## Додаємо нову тему

У функції __start__ створена клавіатура __InlineKeyboardMarkup__, в якій вказані всі теми. 
``` python
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
```

Щоб додати нову тему, треба додати нову кнопку. Створімо змінну __literature_btn__ за аналогією до тих, що вже є, і присвоїмо їй значення за допомогою подуля __types__ 

```python
literature_btn = types.InlineKeyboardButton(text = 'Література', callback_data = 'topic6')
```
Параметру __callback_data__ ми ставимо у відповідність довільне значення, яку потім використовуватимемо для зв'язку зі створеною кнопкою.

Додамо __literature_btn__ до списку кнопок і передамо її як шосту змінну в __topics_kb.add__, таким чином додавши до клавіатури. У підсумку функція __start__ матиме такий вигляд:

``` python
def start(message):
    topics_kb = types.InlineKeyboardMarkup(row_width = 1)
    physics_btn = types.InlineKeyboardButton(text = 'Фізика', callback_data = 'topic1')
    maths_btn = types.InlineKeyboardButton(text = 'Математика', callback_data = 'topic2')
    geography_btn = types.InlineKeyboardButton(text = 'Географія', callback_data = 'topic3')
    astronomy_btn = types.InlineKeyboardButton(text = 'Аcтрономія', callback_data = 'topic4')
    common_btn = types.InlineKeyboardButton(text = 'Загальні запитання', callback_data = 'topic5')
    literature_btn = types.InlineKeyboardButton(text = 'Література', callback_data = 'topic6')
    topics_kb.add(physics_btn, maths_btn, geography_btn, astronomy_btn, common_btn, literature_btn)
    greeting = f'''Привіт, <i>{message.from_user.first_name}</i>! Мене звати <b>Сонях🌻</b>. Я - бот, що відповідає на твої запитання. Обери тему, яка тобі потрібна❤️'''

    greeting_mess = bot.send_message(message.chat.id, greeting, reply_markup = topics_kb, parse_mode='html')
    time.sleep(10)
    bot.delete_message(message.chat.id, greeting_mess.id)
```
## Додаємо нові завдання
#### Якщо додаємо завдання до нової теми
У функції __check_callback_topics__ маємо клавіатуру __ReplyKeyboardMarkup__, яка містить у собі всі завдання кожної з тем. Нам треба створити нову клавіатуру __literature_kb__, яка міститиме всі завдання теми _Література_. Ця клавіатура з'являтиметься після натискання кнопки _Література_ в інлайн-клавіатурі, саме для реалізації цієї можливості в попередній функції ми використовували параметр __callback_data__. 

Ми помістимо цей шматок коду під кодом з клавіатурою з теми _Загальні запитання_, тому почнемо з __elif__. Далі змінній __callback.data__ ми передаємо значення __'topic6'__, тобто те саме, яке вказували в кнопці у функції __start__.

```python
elif callback.data == 'topic6': 
```
Далі створюємо маркап-клавіатуру. Для цього вказуємо її назву, кількість кнопок у рядку (__row_width__) і чи хочемо ми змінити розмір клавіатури від стандартного (__resize_keyboard__):
```python
elif callback.data == 'topic6':
        physics_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
```
Тепер треба написати кнопки __literature_btn_1__ та __literature_btn_2__, в параметрі __text__ вказавши наші завдання:
```python
elif callback.data == 'topic6':
        literature_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        literature_btn_1 = types.KeyboardButton(text = 'Назвати відомих шістдесятників')
        literature_btn_2 = types.KeyboardButton(text = 'Цікаві факти про Івана Франка')
```
Додамо наші кнопки в клавіатуру за допомогою методу __add__.

```python
elif callback.data == 'topic6':
        literature_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        literature_btn_1 = types.KeyboardButton(text = 'Назвати відомих шістдесятників')
        literature_btn_2 = types.KeyboardButton(text = 'Цікаві факти про Івана Франка')
        literature.add(literature_btn_1, literature_btn_2)
```
Залишилося лише відправити повідомлення за допомогою методу __send_message__, в якому ми записуємо текст повідомлення бота про обрану тему і третім параметром вказуємо клавіатуру із завданнями:
```python
elif callback.data == 'topic6':
        literature_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        literature_btn_1 = types.KeyboardButton(text = 'Назвати відомих шістдесятників')
        literature_btn_2 = types.KeyboardButton(text = 'Цікаві факти про Івана Франка')
        literature.add(literature_btn_1, literature_btn_2)
        bot.send_message(callback.message.chat.id, '''"Слова та голос — більш нічого. А серце б’ється, ожива, Як їх почує!" - писав іще Шевченко. <b>Література</b>📚📝 - чудовий вибір! В цій темі є два запитання. Вибери, яке тобі потрібно❤️''', reply_markup = physics_kb, parse_mode='html')
```

Тепер функція __check_callback_topics__ має наступний вигляд:

```python
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
    elif callback.data == 'topic6':
        literature_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        literature_btn_1 = types.KeyboardButton(text = 'Назвати відомих шістдесятників')
        literature_btn_2 = types.KeyboardButton(text = 'Цікаві факти про Івана Франка')
        literature.add(literature_btn_1, literature_btn_2)
        bot.send_message(callback.message.chat.id, '''"Слова та голос — більш нічого. А серце б’ється, ожива, Як їх почує!" - писав іще Шевченко. <b>Література</b>📚📝 - чудовий вибір! В цій темі є два запитання. Вибери, яке тобі потрібно❤️''', reply_markup = physics_kb, parse_mode='html')
```
<a id='anchor'></a>
Далі у функцію __answers__ нам треба додати відповіді на дані запитання. 

Ми додамо цей блок коду перед __else__, тому починаємо його з __elif__:
```python 
elif message.text == 'Назвати відомих шістдесятників':
```
Далі створюємо змінну __а__, якій передаємо значення __types.ReplyKeyboardRemove()__, це дозволить нам видалити клавіатуру з завданнями.
```python 
elif message.text == 'Назвати відомих шістдесятників':
       a = types.ReplyKeyboardRemove()
```
Далі за допомогою методу __send_message__ надсилаємо відповідь на поставлене запитання, вказавши третім параметром клавітуру __а__ (тобто фактично видалену клавіатуру):
```python
elif message.text == 'Назвати відомих шістдесятників':
       a = types.ReplyKeyboardRemove()
       bot.send_message(message.chat.id, '''Основу руху шістдесятників склали письменники Іван Драч, Микола Вінграновський, Володимир Дрозд, Григір Тютюнник, Борис Олійник, Віталій Дончик, Василь Симоненко,Микола Холодний, Ліна Костенко, Валерій Шевчук та инші.''', reply_markup = a)
```
Аналогічно для другого запитання:
```python
elif message.text == 'Цікаві факти про Івана Франка':
       a = types.ReplyKeyboardRemove()
       bot.send_message(message.chat.id, '''1. Мати Івана Франка, Марія Кульчицька, походила із зубожілого українського шляхетського роду Кульчицьких, гербу Сас, була на 33 роки молодшою за чоловіка. Померла, коли Іванові було 15 років.

2. Коли Франкові було 9 років, помер батько. Мати вийшла заміж удруге. Вітчим, Гринь Гаврилик, уважно ставився до дітей, фактично замінив хлопцеві батька. Франко підтримував дружні стосунки зі своїм вітчимом протягом всього життя.

4. Навчаючись у Дрогобицькій гімназії, Франко жив на квартирі в далекої родички Кошицької на околиці міста. Нерідко спав у трунах, які виготовлялися у її столярній майстерні (“У столярні”)

5. Восени 1875 року Франко став студентом філософського факультету Львівського університету. Спочатку належав до москвофільського товариства. Москвофільство було дуже популярне серед галицької інтелігенції в другій половині ХІХ століття. Москвофілом був також один із засновників “Руської Трійці” Яків Головацький.''', reply_markup = a)
```  
#### Якщо додаємо завдання до теми, яка вже існує

Додамо запитання _Який океан найбільший за площею?_ до теми _Географія_. Для цього повернемося у функцію __check_callback_topics__, у блок __elif callback.data == 'topic3'__, який відповідає за географію. Додамо нову кнопку, на якій буде написано додане завдання:
```python
elif callback.data == 'topic3':
        geography_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        geography_btn_1 = types.KeyboardButton(text = '5 найвищих гір світу')
        geography_btn_2 = types.KeyboardButton(text = 'Дві держави, що мають найбільшу кількість кордонів з іншими державами')
        geography_btn_3 = types.KeyboardButton(text = 'Найбільш населене місто світу')
        geography_btn_4 = types.KeyboardButton(text = 'Дві держави, які мають найбільшу кількість водосховищ в світі')
        geography_btn_5 = types.KeyboardButton(text = 'Який океан найбільший за площею?')
```
Додаємо кнопку в клавіатуру за допомогою методу __add__ (просто дописуємо її як п'ятий параметр) 
```python
elif callback.data == 'topic3':
        geography_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        geography_btn_1 = types.KeyboardButton(text = '5 найвищих гір світу')
        geography_btn_2 = types.KeyboardButton(text = 'Дві держави, що мають найбільшу кількість кордонів з іншими державами')
        geography_btn_3 = types.KeyboardButton(text = 'Найбільш населене місто світу')
        geography_btn_4 = types.KeyboardButton(text = 'Дві держави, які мають найбільшу кількість водосховищ в світі')
        geography_btn_5 = types.KeyboardButton(text = 'Який океан найбільший за площею?')
        geography_kb.add(geography_btn_1, geography_btn_2, geography_btn_3, geography_btn_4, geography_btn_5)
```
Надсилаємо повідомлення разом з клавіатурою запитань з теми _Географія_:
```python
elif callback.data == 'topic3':
        geography_kb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
        geography_btn_1 = types.KeyboardButton(text = '5 найвищих гір світу')
        geography_btn_2 = types.KeyboardButton(text = 'Дві держави, що мають найбільшу кількість кордонів з іншими державами')
        geography_btn_3 = types.KeyboardButton(text = 'Найбільш населене місто світу')
        geography_btn_4 = types.KeyboardButton(text = 'Дві держави, які мають найбільшу кількість водосховищ в світі')
        geography_btn_5 = types.KeyboardButton(text = 'Який океан найбільший за площею?')
        geography_kb.add(geography_btn_1, geography_btn_2, geography_btn_3, geography_btn_4, geography_btn_5)
        bot.send_message(callback.message.chat.id, 'Любиш подорожувати? 
        <b>Географія🗺🧭</b> - прекрасний вибір! В цій темі я маю чотири запитання. Що тебе цікавить?', reply_markup = geography_kb, parse_mode='html')
```
Тепер мусимо додати відповідь на наше запитання у функцію __answers__. Аналогічно до [зразка](#anchor) створюємо блок з відповіддю:

```python
elif message.text == 'Який океан найбільший за площею?':
       a = types.ReplyKeyboardRemove()
       bot.send_message(message.chat.id, '''Всім відомо, що найбільший океан планети ― це Тихий. Його площа становить майже 178 мільйонів квадратних кілометрів, і це майже половина світового океану. З півдня на північ він простягнувся на 16 тисяч кілометрів, а із заходу на схід — майже на 20 тисяч.''', reply_markup = a)
```

