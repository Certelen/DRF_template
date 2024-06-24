# DRF_template

## Описание
Данный сервис позволяет парсить с сайта www.farpost.ru первые 10 объявлений по запросу Видеонаблюдение и выдавать их по API запросу.

## Технологии
- Python 3.11
- Django 5.0.6
- DRF 3.15.2
- Selenium 4.22.0

# Установка
## Копирование репозитория
Клонируем репозиторий и переходим в папку проекта:
```
~ git clone git@github.com:Certelen/DRF_template.git
~ cd DRF_template
```

## Развертывание на текущем устройстве:
Устанавливаем и активируем виртуальное окружение из папки с проектом
```
~ python -m venv venv
~ . venv/Scripts/activate
```
Устанавливаем требуемые зависимости:
```
~ pip install -r requirements.txt
```
Переходим в папку
```
~ cd drf_project
```
Перед первым запуском создаем и выполняем миграции:
```
python manage.py makemigrations api
python manage.py migrate
```
Создаем суперпользователя, если необходимо:
```
python manage.py createsuperuser
```
# Заполнение .env
Создайте файл .env и заполните его следующими переменными при необходимости:
```
BROWSER_LOCATION = <Прямой путь до файла с Google Chrome>
CRON = <Для Windows - не заполнять, для Linux - True если создать задачу для обновления объявлений каждый час>
```
# Запуск
Если включен CRON, то добавляем очередь:
```
~ python manage.py crontab add
```
Запуск сервиса производится командой:
```
~ python manage.py runserver
```

# Описание проекта
На сайте www.farpost.ru есть встроенная защита от роботов, которая не обходится заголовками в bs4. При использовании Selenium защита периодически не работает и данные можно спарсить.
При включенном параметре CRON - парсер будет самостоятельно парсить каждый час. При отключенном параметре - только при запросе пользователем объявлений и если прошло больше часа. Однако при включать CRON можно только на Linux. На Windows будет ошибка.
Для доступа к запросу объявлений нужна регистрация и авторизация.

# Адресные пути
- [Регистрация](http://127.0.0.1:8000/auth/users/)
- [Создание токена (на 1 день)](http://127.0.0.1:8000/auth/jwt/create/)
- [Получение данных с сайта (Если прошло больше 1 часа с момента обновления) и вывод.](http://127.0.0.1:8000/api/v1/ads/)

