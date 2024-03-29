"""
WSGI config for dashboardapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from utils.firebase_client import prepare_credentials
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpmecorona.settings.dev")

application = get_wsgi_application()

prepare_credentials()