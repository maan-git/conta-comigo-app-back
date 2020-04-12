import os
from rest_framework import serializers
from app.models.user import User
from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from utils.firebase_client import upload_file
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "addresses")


class Base64ImageFieldReturnUrl(Base64ImageField):
    def to_representation(self, field_value):
        return field_value


class UserSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("addresses", "last_login", "is_active")

    avatar = Base64ImageFieldReturnUrl(required=False)

    @classmethod
    def save_user_avatar(cls, validated_data, user_id: int):
        if 'avatar' not in validated_data.keys():
            return None
        avatar = validated_data.pop('avatar')
        if avatar is not None:
            ext = os.path.splitext(avatar.name)[1]
            file_path = 'Avatars/{}{}'.format(user_id, ext)
            file_content = avatar.file.read()
            file_url = upload_file(settings.FIREBASE_STORAGE_BUCKET,
                                   file_path,
                                   file_content,
                                   avatar.content_type,
                                   True)
            return file_url
        else:
            return None

    @atomic
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user_avatar = self.save_user_avatar(validated_data, user.id)
        if user_avatar:
            user.avatar = user_avatar
        user.save()

        return user

    def update(self, instance, validated_data):
        user_avatar = self.save_user_avatar(validated_data, instance.id)
        if user_avatar:
            validated_data['avatar'] = user_avatar
        return super().update(instance, validated_data)
