from .base import *

DEBUG=True

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        }
    }

"""
    'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB', default='myshop'),
        'USER': config('POSTGRES_USER', default='myshop'),
        'PASSWORD': config('POSTGRES_PASSWORD', default='myshop'),
        'HOST': config('POSTGRES_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='5432'),
"""