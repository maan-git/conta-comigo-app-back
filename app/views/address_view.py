from rest_framework.viewsets import ModelViewSet
from app.models.address import Address
from utils.views_utils import get_generic_read_serializer


class AddressView(ModelViewSet):
    queryset = Address.objects.all()
    ordering = ("name",)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Address, 1)
        return serializer_class
