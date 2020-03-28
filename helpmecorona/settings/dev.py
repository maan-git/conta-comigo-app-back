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
# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
#         "USER": os.environ.get("SQL_USER", "user"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#         # "HOST": os.environ.get("SQL_HOST", "localhost"),
#         "HOST": '192.168.1.2',
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#     }
# }


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.environ.get("SQL_DATABASE", "contacomigo_dev"),
        "USER": os.environ.get("SQL_USER", "contacomigo_user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "P@$$worD"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

WSGI_APPLICATION = 'helpmecorona.wsgi-dev.application'
