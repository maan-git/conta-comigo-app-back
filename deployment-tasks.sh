#!/bin/bash

# Delpoyment tasks

python manage.py migrate
python manage.py loaddata help_0001_help_category help_0002_help_request_status help_0003_helping_status help_0004_help_request_cancel_reason app_0001_global_variable_type app_0002_brazilian_states app_0003_global_variable
python manage.py loadaddresses app/data/addresses.zip --verbositylevel 0