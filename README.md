# Веб-приложение - планировщик задач


## Описание проекта:
Проект позволяет пользователю ставить перед собой цели и задачи, планировать их
выполнение и фиксировать результат. Архивировать выполненные задачи.

## Стек технологий
1. python3.10
2. Django
3. Postgres

### Разворачивание проекта
01. Клонировать проект из репозитория.
02. Создать виртуальное окружение.
03. Установить менеджер пакетов POETRY  (**pip install poetry**).
04. Выполнить команду **poetry update** для установки необходимых пакетов и зависимостей.
05. Создать в корне проекта файл **.env** по примеру файла **.env_example** и определить в нём
соответствующие настройки переменных окружения.


   - **DEBUG**=True (Для PROD сервера должен быть установлен в False)
   - **SECRET_KEY**=*Секретный ключ* (сгенерируйте новый ключ для вашей версии проекта)
   - **DB_NAME**=*название БД*
   - **DB_USER**=*имя пользователя БД*
   - **DB_PASSWORD**=*пароль для подключения к БД*
   - **DB_HOST**=*хост размещения БД*
   - **DB_PORT**=*порт на котором работает БД*
   - **DATABASE_URL**=postgres://user:password@localhost:5432/db_name


06. Создать базу данных (**docker-compose up -d**).
07. Инициализируем миграции если они не сделаны (**python manage.py makemigrations**)
08. Накатываем миграции в БД (**python manage.py migrate**)
09. Создаём суперпользователя для админки (**python manage.py createsuperuser**)
10. Запускаем проект (**python manage.py runserver**)

:hammer:
20:10
