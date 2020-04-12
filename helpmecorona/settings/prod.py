# Import all configuration from base config file
from .base import *
import dj_database_url


# Cors allowed sources
# TODO Configure to production
CORS_ORIGIN_WHITELIST = ("localhost:80", "localhost:8080", "localhost:8081")

# Read the database values from environment variable DATABASE_URL in format:
# postgres://username:password@server:port/database
DATABASES = {
    # Read the database values from environment variable DATABASE_URL in format:
    # postgres://username:password@server:port/database
    "default": dj_database_url.config(conn_max_age=600)
}

WSGI_APPLICATION = "helpmecorona.wsgi-prod.application"

FIREBASE_STORAGE_BUCKET = 'conta-comigo-app-files.appspot.com'

django_heroku.settings(locals(), databases=False, logging=False)
