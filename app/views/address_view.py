from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema, AutoSchema
import coreschema
import coreapi

from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from app.models.address import Address
from utils.views_utils import get_generic_read_serializer


class AddressView(ModelViewSet):
    queryset = Address.objects.all()
    ordering = ("name",)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Address, 1)
        return serializer_class

    @action(methods=["post"],
            detail=True,
            url_path="addresbyzip",
            schema=ManualSchema(description='ZIP code',
                                fields=[
                                    coreapi.Field(
                                        "zip",
                                        required=True,
                                        location="path",
                                        schema=coreschema.Integer(),
                                        description='Zip'
                                    )])
            )
    def get_address_by_zip(self, request: Request, pk):
        address = Address.objects.filter(zip=request.data.zip).first()
        return address
