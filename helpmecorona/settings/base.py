"""
Django settings for helpmecorona project.

Generated by 'django-admin startproject' using Django 2.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import dj_database_url

from corsheaders.defaults import default_headers
from rest_framework.settings import ISO_8601

##################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
##################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g3dm$@^@dfq3zqia4ito+c%2vuo%r$&1eg(7b#y5)s$=t469jz'

ALLOWED_HOSTS = ['*', 'herokudjangoapp.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'app',
    'help'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helpmecorona.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# TODO change
AUTH_USER_MODEL = "app.User"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'helpmecorona.authentication.custom_session_authentication.CustomSessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 9999999,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',
                                'rest_framework.filters.OrderingFilter'),
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    # 'DATE_FORMAT': ISO_8601,
    'DATE_INPUT_FORMATS': ('%Y/%m/%d %H:%M',
                           '%m/%d/%Y %H:%M',
                           '%d/%m/%Y %H:%M',
                           '%Y/%m/%d',
                           '%m/%d/%Y',
                           '%d-%m-%Y',
                           '%d/%m/%Y',
                           ISO_8601),

    # 'DATETIME_FORMAT': ISO_8601,
    'DATETIME_INPUT_FORMATS': ('%Y/%m/%d %H:%M',
                               '%m/%d/%Y %H:%M',
                               '%d/%m/%Y %H:%M',
                               ISO_8601),

    # 'TIME_FORMAT': ISO_8601,
    'TIME_INPUT_FORMATS': (ISO_8601, "%H:%M:%S"),
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SAMESITE = None

CORS_ALLOW_HEADERS = default_headers + (
    'x-requested-with',
    'Access-Control-Allow-Headers'
)
CORS_ALLOW_CREDENTIALS = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

APPEND_SLASH = False

# Cors allowed sources
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:80',
#     'http://localhost:8080',
#     'http://localhost:8081'
# )

STATIC_ROOT = os.path.join(BASE_DIR, "static")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout,
            'filters': ['require_debug_true']
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/general.log',
            'when': 'd',
            'interval': 1,
            'backupCount': 10,
            'formatter': 'simple'
        },
    },
    "loggers": {
        # "": {
        #     "handlers": ["console", 'file'],
        #     'level': 'INFO',
        # },
        "django": {
            "handlers": ["console"],
            'level': 'INFO',
        },
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['console'],
        }
    }
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': True,
    'JSON_EDITOR': False,
    'SECURITY_DEFINITIONS': None,
    'OPERATIONS_SORTER': 'alpha',
    'APIS_SORTER': 'alpha',
    'DOC_EXPANSION': 'list',
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout'
}

# Prefix to swagger urls
# TODO check if will be needed in production
SWAGGER_API_PREFIX = ''
