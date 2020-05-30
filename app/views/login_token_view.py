import coreapi
from django.contrib.auth import login
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from utils.views_utils import get_param_or_400
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from app import decrypt_pass


class LoginTokenView(ObtainAuthToken):
    permission_classes = (AllowAny,)

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("username", description="User email"),
            coreapi.Field("password", description="User password"),
        ]
    )

    def post(self, request: Request, *args, **kwargs):
        """
        Authenticate an user returning a token.
        """
        password = get_param_or_400(request.data, "password", str)

        # Decrypt the password
        password = decrypt_pass(password)
        request.data["password"] = password

        result = super().post(request, *args, **kwargs)
        return result
