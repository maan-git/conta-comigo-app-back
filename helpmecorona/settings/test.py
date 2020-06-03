# Import all configuration from base config file
from .base import *
import dj_database_url

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

# Cors allowed sources
# TODO Configure to test
CORS_ORIGIN_WHITELIST = (
    "http://localhost",
    "http://test.helpmecorona.com",
    "http://localhost:80",
    "http://localhost:8080",
    "http://localhost:8081",
    "https://localhost",
    "https://localhost:80",
    "https://localhost:8080",
    "https://localhost:8081",
    "https://www.test.contacomigoapp.com.br",
    "https://test.contacomigoapp.com.br"
)

DATABASES = {
    # Read the database values from environment variable DATABASE_URL in format:
    # postgres://username:password@server:port/database
    "default": dj_database_url.config(
        conn_max_age=600,
        default="postgres://contacomigotest:12345@localhost:5432/contacomigo_test",
    )
}


FIREBASE_STORAGE_BUCKET = 'staging.conta-comigo-app-files.appspot.com'

# TODO put correct value
OUTPUT_EMAILS_SENDER = 'contacomigoapp@gmail.com'
