from google.cloud import storage
from google.cloud.storage import Bucket


def upload_file(bucket_name: str, file_path: str, file_bytes: bytes, mime_type: str, public: bool) -> str:
    storage_client = storage.Client()
    bucket: Bucket = storage_client.bucket(bucket_name)

    new_file = bucket.blob(file_path)
    new_file.upload_from_string(file_bytes, content_type=mime_type)

    if public:
        new_file.make_public()

    return new_file.public_url

