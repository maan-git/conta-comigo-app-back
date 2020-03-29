# Import all configuration from base config file
from .base import *


# Cors allowed sources
# TODO Configure to production
CORS_ORIGIN_WHITELIST = ("localhost:80", "localhost:8080", "localhost:8081")

WSGI_APPLICATION = "helpmecorona.wsgi-prod.application"
