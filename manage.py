#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpmecorona.settings.dev")
    os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS",
                          "./extra_files/google_credentials/contacomigo-backend@conta-comigo-app-files.iam.gserviceaccount.com.json")

    google_credentials_content = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_CONTENT')
    google_credentials_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

    logging.info('Checking if google credentials info is complete')
    if google_credentials_content and google_credentials_path:
        logging.info('Starting google credentials file generations')
        with open(google_credentials_path, 'w') as credentials_file:
            credentials_file.write(google_credentials_content)
            credentials_file.close()
            logging.info('Google credentials file generated successfully')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
