from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser


class AdminEditOnlyView(ModelViewSet):
    def get_permissions(self):
        """
       Instantiates and returns the list of permissions to allow only admins to edit this view data.
       """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
