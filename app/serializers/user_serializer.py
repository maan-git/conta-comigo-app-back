import os
import uuid
from rest_framework import serializers
from app.models.user import User
from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from utils.firebase_client import (upload_file, delete_file, read_file)
from django.conf import settings
from app.serializers.user_address_serializer import UserAddressSerializer
from app.models.user import DEFAULT_USER_IMAGE_URL

from cryptography.fernet import Fernet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class Base64ImageFieldReturnUrl(Base64ImageField):
    def to_representation(self, field_value):
        return field_value


class UserSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("addresses", "last_login", "is_active")

    avatar = Base64ImageFieldReturnUrl(required=False)

    @classmethod
    def consult_user_avatar(cls, user: User):
        print('Consult the image..')
        user_avatar_name = user.avatar.split('/')[-1]
        user_avatar_folder = user.avatar.split('/')[-2]
        return read_file(settings.FIREBASE_STORAGE_BUCKET,
                         user_avatar_folder, user_avatar_name)

    @classmethod
    def delete_user_avatar(cls, user: User):
        print('Deleting the image..')
        user_avatar_name = user.avatar.split('/')[-1]
        user_avatar_folder = user.avatar.split('/')[-2]
        return delete_file(settings.FIREBASE_STORAGE_BUCKET,
                           f'{user_avatar_folder}/{user_avatar_name}')

    @classmethod
    def save_user_avatar(cls, validated_data):
        print('Saving the image..')
        avatar = validated_data.pop('avatar')
        if avatar is not None:
            ext = os.path.splitext(avatar.name)[1]
            file_name = str(uuid.uuid4())
            file_path = f'Avatars/{file_name}{ext}'
            file_content = avatar.file.read()
            file_url = upload_file(settings.FIREBASE_STORAGE_BUCKET,
                                   file_path,
                                   file_content,
                                   avatar.content_type,
                                   True)
            return file_url
        else:
            return None

    @classmethod
    def change_user_image(cls, validated_data, user: User):
        if 'avatar' not in validated_data.keys():
            return None

        if user.avatar != DEFAULT_USER_IMAGE_URL and user.avatar.__class__.__name__ != 'ContentFile':
            if cls.consult_user_avatar(user):
                if not cls.delete_user_avatar(user):
                    raise Exception("Error during changing the user avatar..")
        return cls.save_user_avatar(validated_data)

    def process_special_fields(self, validated_data, user: User):
        if 'password' in validated_data:
            password = validated_data.pop("password")
            user.set_password(password)

        user_avatar = self.change_user_image(validated_data, user)

        if user_avatar:
            user.avatar = user_avatar

    @atomic
    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        # Password
        user.password = self.decrypt_pass(user.password)

        self.process_special_fields(validated_data, user)
        user.save()
        return user

    def update(self, instance, validated_data):
        self.process_special_fields(validated_data, instance)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        result = super().to_representation(instance)

        # Remove password from serialized object
        if 'password' in result:
            result.pop('password')

        return result

    def decrypt_fernet(self, pass_str):
        try:
            fernet_ = Fernet(os.environ.get('SECRET_KEY_PASS', ''))
            return fernet_.decrypt(pass_str)
        except Exception as ex:
            print(f"Error: {ex}")

    @classmethod
    def decrypt_pass(self, pass_str):
        decoded_text = self.get_fernet_obj(pass_str)
        res = []
        pas_ = decoded_text.split('95')[:-1]
        for x, pas in enumerate(pas_):
            res.append(chr(((x - (len(pas_) + 1)) - int(pas)) * -1))
        return ''.join(res)


class UserSerializerCurrentUser(UserSerializer):
    addresses = UserAddressSerializer(many=True, read_only=True)
