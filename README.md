<pre>
Настроить apiproject/settings.py

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'apidb', //имя БД
    'USER': 'postgres', //имя пользщователя БД
    'PASSWORD': '1234',
    'HOST': 'localhost', # Set to empty string for localhost.
    'PORT': '5432', # Set to empty string for default.
    }
}
//
Для начало нужно добавить значения в БД через /api/

При методе GET и DELETE - ключевое поле тут id. Остлаьные поля не активны
При методе POST поле id не играет роль, его можно не заполнять

//
/api/ - поля для ввода получения и удаления записей
/api/program - список всех записей
/api/program/{id} - получение конкретной программы
/api/program/count -колличество записей в БД

(/api/program/) -не правильный адрес
</pre>
