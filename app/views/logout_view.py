from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.authtoken.views import APIView


class LogoutView(APIView):
    @classmethod
    def post(cls, request, *args, **kwargs):
        """
        Logout an user.
        """
        logout(request)
        return Response()
