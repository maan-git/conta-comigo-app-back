# Import all configuration from base config file
from .base import *

# import django_heroku

# django_heroku.settings(locals())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# if os.environ.get('RUN_MAIN', None) != 'true':
#     LOGGING = {}

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'contacomigo_dev',
        'USER': 'contacomigo_user',
        'PASSWORD': 'P@$$worD',
        'HOST': 'localhost'

        
    }
}

WSGI_APPLICATION = 'helpmecorona.wsgi-dev.application'
