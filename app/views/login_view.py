from rest_framework.authtoken.models import Token

import coreapi
from django.contrib.auth import login
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.authtoken.views import APIView
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from utils.views_utils import get_param_or_400
from app.serializers.user_serializer import UserSerializer
from django.contrib.auth import authenticate


class LoginView(APIView):
    permission_classes = (AllowAny,)

    schema = AutoSchema(
        manual_fields=[coreapi.Field('username', description='User email'),
                       coreapi.Field('password', description='User password')]
    )

    @classmethod
    def post(cls, request: Request, *args, **kwargs):
        """
        Authenticate an user.
        """
        username = get_param_or_400(request.data, "username", str)
        password = get_param_or_400(request.data, "password", str)

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            data = UserSerializer(user).data
            data['token'] = Token.objects.get(user=user).key
            return Response(data=data)
            # return Response(data=UserSerializer(user).data)
        else:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))
