# Заготовка

Для команды py masters.
На данный момент созданы все модели, реализованы регистрация, авторизация и выход из аккаунта, и тестовая защищённая страница.
Для запуска проекта:
1) создать виртуальное окружение:
```commandline
py -m venv venv
```
-для виндовс
```commandline
python3 -m venv venv
```
-для линукса
2) активировать:
```commandline
venv\Scripts\activate
```
-для виндовс

```commandline
source venv/bin/activate
```
-для линукса
3) Создать файл .env и там установить ссылку для подключения к бд по следующему паттерну:
```
DATABASE_URL=postgresql+asyncpg://<your_user_name>:<your_password>@localhost:<your_port>/<your_db_name>
```
например
```
DATABASE_URL=postgresql+asyncpg://postgres:123456789@localhost:5432/mydb
```
туда же прописать
```
SECRET_KEY=<your_secret_key>
```
это нужно для шифрования JWT токенов при авторизации.
4) Для создания таблиц в бд запустить models.py:
```commandline
python3 models.py
```

Вот и готово, для запуска проекта 
```commandline
python3 main.py
```
