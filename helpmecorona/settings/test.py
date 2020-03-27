# Import all configuration from base config file
from .base import *

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'HELPMECORONA_TEST',
        'USER': 'postgres',
        'PASSWORD': 'P@$$worD',
        'HOST': 'localhost'
    }
}


WSGI_APPLICATION = 'helpmecorona.wsgi-dev.application'
