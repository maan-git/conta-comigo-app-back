# Import all configuration from base config file
from .base import *

# TODO Configure silk
# MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'df040sn040cto4',
        'USER': 'wpnvxytmgcvtds',
        'PASSWORD': 'b291ba359c3a1f66eb00df9cd734c59c520b59aa5ababf31ee30013d3932947f',
        'HOST': 'ec2-34-200-101-236.compute-1.amazonaws.com',
        'PORT': 5432
    }
}


WSGI_APPLICATION = 'helpmecorona.wsgi-dev.application'
