# Import all configuration from base config file
from .base import *

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
        'NAME': 'HELPMECORONA_DEV',
        'USER': 'postgres',
        'PASSWORD': 'P@$$worD',
        'HOST': 'localhost'
    }
}


WSGI_APPLICATION = 'helpmecorona.wsgi-dev.application'
