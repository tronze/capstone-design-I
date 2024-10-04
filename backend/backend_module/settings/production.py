import os

from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = []

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DB_NAME'],
    'HOST': os.environ['DB_HOST'],
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PASSWORD'],
    'PORT': os.environ['DB_PORT'],
}

WSGI_APPLICATION = 'backend_module.wsgi.production.application'
