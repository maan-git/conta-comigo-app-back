# Import all configuration from base config file
from .base import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'HELPMECORONA_PROD',
        'USER': 'postgres',
        'PASSWORD': 'P@$$worD',
        'HOST': 'localhost'
    }
}

# TODO Configure to production
CORS_ORIGIN_WHITELIST = (
    'localhost:80',
    'localhost:8080',
    'localhost:8081'
)

WSGI_APPLICATION = 'helpmecorona.wsgi-prod.application'