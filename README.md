# Тестировщик на Django
Сервис проведения тестирования по каким-либо темам. Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат.
- Добавляйте / обновляйте / удаляйте вопросы от администратора.

# Запуск проекта без Docker

1. ```Клонировать репозиторий https://github.com/Denis-Guselnikov/test_app```
2. ```cd test_app/```
3. ```Создаёте виртуальное окружение```
4. ```pip install -r requirements.txt```
5. ```Создать и заполнить .env - файл должен находится в testapp```

## Образец:
```
DB_ENGINE=django.db.backends.postgresql  # указываем, что работаем с postgresql
DB_NAME=db_name  # имя базы данных
POSTGRES_USER=db_user  # логин для подключения к базе данных
POSTGRES_PASSWORD=db_password  # пароль для подключения к БД (установите свой)
DB_HOST=db_host  # название сервиса (контейнера)
DB_PORT=5432  # порт для подключения к БД
```
## База Данных

В репозитории есть db.sqlite3

6. ```cd testapp/```
7. ```python manage.py runserver```

```
login: admin
password: admin
```

# Запуск с помощью Docker

Убедитесь, что вы находитесь в той же директории, где сохранён Dockerfile

1. ```Клонировать репозиторий https://github.com/Denis-Guselnikov/test_app```
2. ```docker build -t testapp .```
3. ```docker run --name testapp -it -p 8000:8000 testapp```

Проект доступен: ```http://127.0.0.1:8000/```
