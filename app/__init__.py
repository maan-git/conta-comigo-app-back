import os
import datetime
import random
import string

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
        raise


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
        raise


def encrypt_fernet(pass_str):
    try:
        key_ = os.environ.get('SECRET_KEY_PASS', '')
        key_b_ = bytes(key_, 'utf-8')
        fernet_ = Fernet(key_b_)
        res = fernet_.encrypt(bytes(pass_str, 'utf-8'))
        res = str(res, 'utf-8')
        return res

    except Exception as ex:
        print(f"Error encrypting the password through Fernet: {ex}")
        raise


def encrypt_pass(pass_str):
    try:
        res = []
        num_ = ord("_")
        for x, _ in enumerate(pass_str):
            res_ = [(x - (len(pass_str) + 1)) + ord(_), num_]
            res.append(''.join(map(str, res_)))
        res_encrypt = encrypt_fernet(''.join(res))

        return res_encrypt
    except Exception as ex:
        print(f"Error encrypting the password with our own method: {ex}")
        raise


def generate_new_pass(user_obj):
    try:
        len_pass = random.randint(10, 15)
        password_characters = string.ascii_letters + string.digits + string.punctuation
        _ = ''.join(random.choice(password_characters) for i in range(len_pass))
        __ = list(user_obj.first_name + user_obj.last_name)
        __len = int(len(__) / 2)
        _ = list(_)
        for x in range(3):
            _.insert(int(len_pass / 3) * x + 1, __[__len + x])

        new_pass = ''.join(_)
        return new_pass
        # return encrypt_pass(new_pass)

    except Exception as ex:
        print(f"Error making a new password: {ex}")
        raise
