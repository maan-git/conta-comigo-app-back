# Import all configuration from base config file
from .base import *

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

# Cors allowed sources
# TODO Configure to test
CORS_ORIGIN_WHITELIST = (
    "http://localhost:80",
    "http://localhost:8080",
    "http://localhost:8081",
    "https://localhost:80",
    "https://localhost:8080",
    "https://localhost:8081",
)


WSGI_APPLICATION = "helpmecorona.wsgi-test.application"
