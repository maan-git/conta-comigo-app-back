# Import all configuration from base config file
from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# if os.environ.get('RUN_MAIN', None) != 'true':
#     LOGGING = {}

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

CORS_ORIGIN_ALLOW_ALL = True

# If environment is not set, don't initialize the databases objects, since it may be running under docker and
# The values may come from env file
DATABASES = {
    # Read the database values from environment variable DATABASE_URL in format:
    # postgres://username:password@server:port/database
    "default": dj_database_url.config(
        conn_max_age=600,
        default="postgres://contacomigo_user:12345@db:5432/contacomigo_dev",
    )
}

FIREBASE_STORAGE_BUCKET = 'staging.conta-comigo-app-files.appspot.com'

OUTPUT_EMAILS_SENDER = 'contatodev@contacomigoapp.com.br'
