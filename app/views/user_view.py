from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from app.models.user import User
from app.serializers.user_serializer import UserSerializer
from app.serializers.user_serializer import UserSerializerPost
from utils.views_utils import ModelViewSetNoDelete

from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser


class UserView(ModelViewSetNoDelete):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        else:
            return UserSerializerPost

    def get_permissions(self):
        """
       Instantiates and returns the list of permissions that this view requires.
       """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(methods=['get'],
            detail=False,
            url_path='current',
            schema=ManualSchema(fields=[],
                                description='Get the data from the currently logged user'))
    def get_current_user_data(self, request: Request):
        """
        Get the data from the currently logged user
        """
        serializer_class = self.get_serializer_class()

        return Response(data=serializer_class(request.user).data)

    def post(self, request, pk=None, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                photo=request.data.get('avatar')
            )
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
