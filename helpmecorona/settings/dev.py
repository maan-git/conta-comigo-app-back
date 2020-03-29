# Import all configuration from base config file
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# if os.environ.get('RUN_MAIN', None) != 'true':
#     LOGGING = {}

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.environ.get("SQL_DATABASE", "contacomigo_dev"),
        "USER": os.environ.get("SQL_USER", "contacomigo_user_dev"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "contacomigo_pass"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
