# Для работы проекта нужно:
+ Установить rest-framework
+ Настроить apiproject/settings.py
    + //Изменить данные о БД
        +<pre>
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
</pre>
//
