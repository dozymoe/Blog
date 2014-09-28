Blog-Django-Indonesia
=============

Repositori resmi Blog Django indonesia

**UNDER HEAVY DEVELOPMENT**

Gabung Trello Django Developer Indonesia utk kolaborasi bersama : https://trello.com/b/ZheIYEHZ/django-id-blog-development (Email ke alzea.arafat@gmail.com utk meminta invitation ke Trello).

###Settings
Supaya konfigurasi database Anda tidak menimpa `settings.py` yang sudah ada, silakan buat file baru bernama `local_settings.py` pada direktori `portal` dengan isi:
```python
import sys

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nama_database_anda',
        'USER': 'user_database_anda',
        'PASSWORD': 'password_database_anda',
        'HOST': 'localhost',
        'PORT': '',
    }
}

if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
```
