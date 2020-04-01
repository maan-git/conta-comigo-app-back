#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py loaddata help_0001_help_category help_0002_help_request_status help_0003_helping_status

exec "$@"
