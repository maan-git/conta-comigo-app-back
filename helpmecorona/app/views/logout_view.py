from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.authtoken.views import APIView


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Logout an user.
        """
        logout(request)
        return Response()
