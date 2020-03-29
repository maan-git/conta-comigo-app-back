#!/bin/bash

# Delpoyment tasks

python manage.py migrate
python manage.py loaddata help_0001_help_category help_0002_help_request_status help_0003_helping_status