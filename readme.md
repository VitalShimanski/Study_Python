
## ABOUT ME
#### I am Vitaliy Shimanski from Belarus

## AREAS OF INTEREST:
##### Telegram bot
##### Parsing
##### SQLite
##### Algoritms & Data structures

##### Now I am learning Python, SQL and others things
##### I am use Ubuntu 18.04 and Pycharm

# Чат-бот для курсов валют, погоды и общения в Telegram с использованием DialogFlow
### Автор проекта: Виталий Шиманский, телеграм — [@VitaliyShim](https://telegram.me/Vitaliy)
### Цель проекта: создание автономных чат-ботов для мессенджера Телеграм

Боты отвечают пользователю на сообщения о курсах валют, о погоде, а также на другие сообщения. Боты работают на одной базе фраз, которая загружена в DialogFlow. Ботов можно быстро обучить благодаря дополнительно реализованным функциям. Также в ботах реализована отправка сообщений на отдельного бота в телеграме для ошибок.

  
Примечание. Если вы задете сложный вопрос для бота, то бот ничего не ответит.

![](working_bot.gif)

# Как установить
### Этап 1. Получить все авторизационные ключи
#### Этап 1.1 Для запуска бота в Телеграме необходимо:
1) Создать бота для пользователй в telegram через [Отца ботов](https://telegram.me/BotFather) и взять токен для авторизации.
2) Создать бота для сервисных сообщений в telegram через [Отца ботов](https://telegram.me/BotFather) и взять токен для авторизации.
3) Узнать свой ID через [специального бота](https://telegram.me/userinfobot).

#### Этап 1.2 Зарегистрироваться и получить ключ авторизации для Dialogflow:
1) Зарегистрироваться на [сайте](https://dialogflow.com/) сервиса.
2) Создать нового агента — нашего бота в DiaologFlow.
3) На вкладке General установить настройку V2 API и перейти по ссылке в поле 'Service Account' в единую панель управления сервисами Google для получения авторизационного ключа.
4) У вашего сервисного аккаунта необходимо создать ключ и скачать его. Этот ключ авторизации необходимо будет использовать для получения ответов от Dialogflow. 
5) На вкладке IAM у вашего сервисного аккаунта установить роль 'Администратор Dialogflow API'

### Этап 2. Установить переменные окружения
1) telegram_token: токен для основного телеграм-бота;  
2) telegram_token_information_message: токен для сервисного телеграм-бота;
3) chat_id_information_message: id пользователя телеграм, который будет получать сервисные сообщения;  
4) vk_community_token: токен для бота ВКонтакте;
5) project_id: id проекта в dialogflow, который можно взять вкладке 'General' в поле 'Project ID';
6) GOOGLE_APPLICATION_CREDENTIALS: путь для json-файла с ключом авторизации для dialogflow;
7) GOOGLE_CREDENTIALS: данную переменную необходимо использовать только, если вы используете Heroku. В данную переменную необходимо поместить содержимое json-файла авторизации для dialogflow.

### Этап 3. Запустить бота 
#### Пример запуска в консоли
```python
python3 bot-tg.py
```

# Требования
Все требуемые модули указаны в файле requirements.txt  
Для установки запустите команду:
```python
python3 pip install -r requirements.txt
```
# Как создать модель вопрос — ответ в dialogflow
#### Cоздание новой темы разговора
1) На вкладке Intents создать Intent. Это будет отдельной темой для бота.
2) Добавить варианты вопросов и ответов.

#### Создать список быстрых ответов
1) На вкладке Small Talk добавить ответы на самые популярные вопросы.


# CONTACT ME
## Find me on Github https://github.com/VitalShimanski / or just say HELLO at vitalesacha@tut.by
