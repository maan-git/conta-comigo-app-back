# Import all configuration from base config file
from .base import *

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

# Cors allowed sources
# TODO Configure to test
CORS_ORIGIN_WHITELIST = (
    'localhost:80',
    'localhost:8080',
    'localhost:8081'
)


WSGI_APPLICATION = 'helpmecorona.wsgi-test.application'
