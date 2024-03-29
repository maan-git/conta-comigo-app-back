# Import all configuration from base config file
from .base import *
import dj_database_url
import json

# Cors allowed sources
# TODO Configure to production
CORS_ORIGIN_WHITELIST = ("https://www.contacomigoapp.com.br",
                         "https://contacomigoapp.com.br")

# Read the database values from environment variable DATABASE_URL in format:
# postgres://username:password@server:port/database
DATABASES = {
    # Read the database values from environment variable DATABASE_URL in format:
    # postgres://username:password@server:port/database
    "default": dj_database_url.config(
        conn_max_age=600,
        default="postgres://contacomigoprod:12345@localhost:5432/contacomigo_prod",
    )
}

print("Databases: " + json.dumps(DATABASES))

FIREBASE_STORAGE_BUCKET = 'conta-comigo-app-files.appspot.com'

OUTPUT_EMAILS_SENDER = 'contato@contacomigoapp.com.br'
