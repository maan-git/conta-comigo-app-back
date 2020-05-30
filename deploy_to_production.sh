#!/bin/bash

# Clear deploy folder
- sudo rm -r /opt/conta-comigo/prod/back/source/*
# Copy all repository to the deploy folder
- sudo cp -r . /opt/conta-comigo/prod/back/source
# Change dir to deploy folder
- cd /opt/conta-comigo/prod/back/source
- sudo ../virtualenv/bin/bin/pip install -r requirements.txt
- sudo ../virtualenv/bin/python manage.py migrate --settings helpmecorona.settings.prod
- sudo ../virtualenv/bin/python manage.py collectstatic --settings helpmecorona.settings.prod --noinput
- sudo ../virtualenv/bin/python manage.py loaddata help_0001_help_category help_0002_help_request_status help_0003_helping_status help_0004_help_request_cancel_reason app_0001_global_variable_type app_0002_brazilian_states app_0003_global_variable app_0004_notification_types notification_001_email_status --settings helpmecorona.settings.prod
- sudo chown -R contacomigoback:contacomigoback /opt/conta-comigo/prod/back/source
- sudo systemctl restart emperor.uwsgi