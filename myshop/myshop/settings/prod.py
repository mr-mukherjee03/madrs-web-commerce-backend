from decouple import config
from .base import *
import os



DEBUG=True

ADMINS=[
    ('shubh', 'shubhadeephriju@gmail.com'),
]

ALLOWED_HOSTS=['madrs.azurewebsites.net','*']
#ALLOWED_HOSTS = ['localhost','127.0.0.1','myshop.com','www.myshop.com','web','madrs-web-commerce-backend.onrender.com']

CSRF_TRUSTED_ORIGINS = [
    'https://madrs.azurewebsites.net',
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True



#DATABASES={
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': config('POSTGRES_DB'),
#        'USER': config('POSTGRES_USER'),
#        'PASSWORD': config('POSTGRES_PASSWORD'),
#        'HOST': 'db',
#        'PORT': 5432,
#    }
#}

#REDIS_HOST='redis'
#REDIS_PORT=6379
#REDIS_DB=1
#CACHES['default']['LOCATION']= REDIS_URL

import os
import dj_database_url

REDIS_URL = os.getenv("REDIS_URL")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "ssl_cert_reqs": None
            }
        }
    }
}


DATABASES = {
    'default': dj_database_url.config(
        default=None, #os.getenv("DATABASE_URL", "sqlite:///db.sqlite3"),
        conn_max_age=600
    )
}


CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@74.225.171.66:5672/")

