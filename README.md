# habit_tracker_SPA-app


beckend часть приложения для формирования привычек.


#### Вся документация доступна в Swagger и Redoс:

```
http://localhost:8000 /redoc/ или /swagger/
```


1. #### Клонируем репозиторий себе, либо скачиваем zip файл и распаковываем себе на локальную машину

2. #### Создаем виртуальное окружение.

3. #### Устанавливаем зависимости командой:

```
pip install -r requirements.txt
```

4.  #### Для работы нам понадобится установить и настройть базу данных PostgreSQL и брокера Redis 

5. #### Выполняем миграцию командой:

```
python manage.py migrate
```

6. #### Загрузка данных

- Загружаем тестовые данные командой:

```
python manage.py loaddata testdata.json
```

7. #### Запустить сервер командой:

```
python manage.py runserver 8000
```

8. #### Запускаем телеграм бота командой:

```
python manage.py bot_run
```

9. #### Запуск Celery

```
celery -A config worker -l INFO -P eventlet
```

10. #### Запуск celery-beat

```
celery -A config worker --loglevel=info
```
