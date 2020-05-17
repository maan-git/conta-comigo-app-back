import os
from utils.firebase_client import prepare_credentials
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpmecorona.settings.dev")

prepare_credentials()

application = get_wsgi_application()
