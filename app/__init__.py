import os
from cryptography.fernet import Fernet


def decrypt_fernet(pass_str):
    try:
        key_ = os.environ.get('SECRET_KEY_PASS', '')
        key_b_ = bytes(key_, 'utf-8')
        fernet_ = Fernet(key_b_)
        res = fernet_.decrypt(bytes(pass_str, 'utf-8'))
        res = str(res, 'utf-8')
        return res
    except Exception as ex:
        print(f"Error decrypting the password through Fernet: {ex}")


def decrypt_pass(pass_str):
    try:
        decoded_text = decrypt_fernet(pass_str)
        res = []
        pas_ = decoded_text.split('95')[:-1]
        for x, pas in enumerate(pas_):
            res.append(chr(((x - (len(pas_) + 1)) - int(pas)) * -1))
        return ''.join(res)

    except Exception as ex:
        print(f"Error decrypting the password with our own method: {ex}")
