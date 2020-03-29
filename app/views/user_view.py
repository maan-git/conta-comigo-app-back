from rest_framework.viewsets import ModelViewSet
from app.models.user import User
from app.serializers.user_serializer import UserSerializer
from app.serializers.user_serializer import UserSerializerPost
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


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
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
