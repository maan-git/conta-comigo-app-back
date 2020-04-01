from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from app.models.user import User
from app.serializers.user_serializer import UserSerializer
from app.serializers.user_serializer import UserSerializerPost


class UserView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        else:
            return UserSerializerPost

    def get_permissions(self):
        """
       Instantiates and returns the list of permissions that this view requires.
       """
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(methods=["get"],
            detail=False,
            url_path="current",
            schema=ManualSchema(fields=[]))
    def get_current_user_data(self, request: Request):
        """
        Get the data from the currently logged user
        """
        serializer_class = self.get_serializer_class()

        return Response(data=serializer_class(request.user).data)
