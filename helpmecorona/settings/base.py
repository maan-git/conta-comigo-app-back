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
from corsheaders.defaults import default_headers
from rest_framework.settings import ISO_8601
from app.services.address_provider_republica_virtual import ExternalProviderRepVirtual


LOG_LEVEL = os.environ.get('DJANGO_LOG_LEVEL', 'INFO')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "g3dm$@^@dfq3zqia4ito+c%2vuo%r$&1eg(7b#y5)s$=t469jz"

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_swagger",
    "rest_framework.authtoken",
    "django_filters",
    "corsheaders",
    "simple_history",
    "utils",
    "app",
    "help",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = "helpmecorona.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
# TODO change
AUTH_USER_MODEL = "app.User"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "helpmecorona.authentication.custom_session_authentication.CustomSessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 9999999,
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
    ),
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    # 'DATE_FORMAT': ISO_8601,
    "DATE_INPUT_FORMATS": (
        "%Y/%m/%d %H:%M",
        "%m/%d/%Y %H:%M",
        "%d/%m/%Y %H:%M",
        "%Y/%m/%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%d/%m/%Y",
        ISO_8601,
    ),
    # 'DATETIME_FORMAT': ISO_8601,
    "DATETIME_INPUT_FORMATS": (
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y/%m/%d %H:%M",
        "%m/%d/%Y %H:%M",
        "%d/%m/%Y %H:%M",
        ISO_8601,
    ),
    # 'TIME_FORMAT': ISO_8601,
    "TIME_INPUT_FORMATS": (ISO_8601, "%H:%M:%S"),
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SAMESITE = None

CORS_ALLOW_HEADERS = default_headers + (
    "x-requested-with",
    "Access-Control-Allow-Headers",
)
CORS_ALLOW_CREDENTIALS = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
    "formatters": {
        "simple": {"format": "%(levelname)s [%(name)s:%(lineno)s] %(message)s"}
    },
    "handlers": {
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": sys.stdout,
            "filters": ["require_debug_true"],
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "logs/general.log",
            "when": "d",
            "interval": 1,
            "backupCount": 10,
            "formatter": "simple",
        },
    },
    "loggers": {
        # "": {
        #     "handlers": ["console", 'file'],
        #     'level': 'INFO',
        # },
        "django": {"handlers": ["console"], "level": LOG_LEVEL},
        "django.db.backends": {"level": "INFO", "handlers": ["console"]},
    },
}

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": True,
    "JSON_EDITOR": False,
    "SECURITY_DEFINITIONS": None,
    "OPERATIONS_SORTER": "alpha",
    "APIS_SORTER": "alpha",
    "DOC_EXPANSION": "list",
    "LOGIN_URL": "rest_framework:login",
    "LOGOUT_URL": "rest_framework:logout",
}

# Prefix to swagger urls
# TODO check if will be needed in production
SWAGGER_API_PREFIX = ""

FIXTURE_DIRS = ("/help/fixtures/", "/app/fixtures/")

MEDIA_URL = "/"

EXTERNAL_ADDRESS_PROVIDER = ExternalProviderRepVirtual
