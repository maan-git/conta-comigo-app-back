# Import all configuration from base config file
from .base import *
import dj_database_url

# Cors allowed sources
# TODO Configure to production
CORS_ORIGIN_WHITELIST = ("localhost:80", "localhost:8080", "localhost:8081",
                         "https://conta-comigo-app-front.herokuapp.com",
                         "https://www.contacomigoapp.com.br",
                         "http://www.contacomigoapp.com.br",
                         "http://contacomigoapp.com.br",
                         "http://contacomigoapp.com.br",)

# Read the database values from environment variable DATABASE_URL in format:
# postgres://username:password@server:port/database
DATABASES = {
    # Read the database values from environment variable DATABASE_URL in format:
    # postgres://username:password@server:port/database
    "default": dj_database_url.config(conn_max_age=600)
}

FIREBASE_STORAGE_BUCKET = 'conta-comigo-app-files.appspot.com'

# TODO put correct value
OUTPUT_EMAILS_SENDER = 'contacomigoapp@gmail.com'
