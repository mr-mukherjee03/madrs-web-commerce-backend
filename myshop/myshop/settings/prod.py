from decouple import config
from .base import *
import os



DEBUG=False

ADMINS=[
    ('shubh', 'shubhadeephriju@gmail.com'),
]

#ALLOWED_HOSTS= os.getenv("ALLOWED_HOSTS", "localhost").split(",")
#ALLOWED_HOSTS = ['localhost','127.0.0.1','myshop.com','www.myshop.com','web','madrs-web-commerce-backend.onrender.com']
ALLOWED_HOSTS = ['*']



DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

#REDIS_HOST='redis'
#REDIS_PORT=6379
#REDIS_DB=1
#CACHES['default']['LOCATION']= REDIS_URL
