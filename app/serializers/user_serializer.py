from rest_framework import serializers
from app.models.user import User
from django.db.transaction import atomic


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)


class UserSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('last_login', 'is_active')

    @atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
