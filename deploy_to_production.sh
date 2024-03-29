#!/bin/bash

# Get password for posrgres user
PG_PASSWORD=$(sudo /root/linuxscripts/get_postgres_password.sh prod)

if [ $? -ne 0 ];
then
  echo "System has failed to get postgres password"
  exit 1
fi
# Set environment variables requires for manage.py commands
export DJANGO_SETTINGS_MODULE=helpmecorona.settings.prod
export DJANGO_STATIC_ROOT=helpmecorona/static
export GOOGLE_APPLICATION_CREDENTIALS_CONTENT="{  \"type\": \"service_account\",  \"project_id\": \"conta-comigo-app-files\",  \"private_key_id\": \"2c2d90afee1426ab87de591b6863ebc9c7820372\",  \"private_key\": \"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADA$"
export DATABASE_URL=postgres://contacomigoprod:$PG_PASSWORD@localhost:5432/contacomigo_prod
export SECRET_KEY_PASS=4IaokWbQcl7RnXdmTqnPaYHkV0m3YZiePSqchMAqwHk=

echo $DATABASE_URL

# Clear deploy folder
rm -r /opt/conta-comigo/prod/back/source/*
# Copy all repository to the deploy folder
cp -r . /opt/conta-comigo/prod/back/source
# Change dir to deploy folder
cd /opt/conta-comigo/prod/back/source
../virtualenv/bin/pip install -r requirements.txt
../virtualenv/bin/python manage.py migrate --settings helpmecorona.settings.prod
../virtualenv/bin/python manage.py collectstatic --settings helpmecorona.settings.prod --noinput
../virtualenv/bin/python manage.py loaddata help_0001_help_category help_0002_help_request_status help_0003_helping_status help_0004_help_request_cancel_reason app_0001_global_variable_type app_0002_brazilian_states app_0003_global_variable app_0004_notification_types notification_001_email_status --settings helpmecorona.settings.prod
chown -R contacomigoback:contacomigoback /opt/conta-comigo/prod/back/source
systemctl restart emperor.uwsgi