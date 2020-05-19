import os
from cryptography.fernet import Fernet


def decrypt_fernet(pass_str):
    try:
        print(f"KEY: {os.environ.get('SECRET_KEY_PASS', '')}")
        key_ = os.environ.get('SECRET_KEY_PASS', '')
        key_b_ = bytes(key_, 'utf-8')
        print(type(key_), type(key_b_))
        fernet_ = Fernet(key_b_)
        return fernet_.decrypt(pass_str)
    except Exception as ex:
        print(f"Error..: {ex}")


def decrypt_pass(pass_str):
    try:
        decoded_text = decrypt_fernet(pass_str)
        print(decoded_text)
        res = []
        pas_ = decoded_text.split('95')[:-1]
        for x, pas in enumerate(pas_):
            res.append(chr(((x - (len(pas_) + 1)) - int(pas)) * -1))
        return ''.join(res)

    except Exception as ex:
        print(f"Error..: {ex}")
