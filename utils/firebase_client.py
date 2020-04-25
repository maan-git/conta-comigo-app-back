import os
import logging
from google.cloud import storage
from google.cloud.storage import Bucket


def read_file(bucket_name: str, file_path: str, file_name: str) -> bool:
    try:
        storage_client = storage.Client()
        bucket: Bucket = storage_client.bucket(bucket_name)

        gcs_file = bucket.get_blob(f'{file_path}/{file_name}')

        return gcs_file
    except Exception as ex:
        logging.exception('Error while consulting file "%s" from bucket "%s"',
                          f'{file_path}/{file_name}',
                          bucket_name)
        logging.exception(ex)
        return False


def upload_file(bucket_name: str, file_path: str, file_bytes: bytes, mime_type: str, public: bool) -> str:
    storage_client = storage.Client()
    bucket: Bucket = storage_client.bucket(bucket_name)

    new_file = bucket.blob(file_path)
    new_file.upload_from_string(file_bytes, content_type=mime_type)

    if public:
        new_file.make_public()

    return new_file.public_url


def delete_file(bucket_name: str, file_path: str) -> bool:
    try:
        storage_client = storage.Client()
        bucket: Bucket = storage_client.bucket(bucket_name)
    except:
        logging.exception('Error while connecting to bucket "%s" to delete file "%s"',
                          bucket_name,
                          file_path)
        return False

    new_file = bucket.blob(file_path)

    try:
        new_file.delete()
    except:
        logging.exception('Error while deleting file "%s" from bucket "%s"',
                          file_path,
                          bucket_name)
        return False

    return True


def prepare_credentials():
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
