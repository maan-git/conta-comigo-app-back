import coreapi
import coreschema
from utils.views_utils import get_generic_read_serializer
from utils.views_utils import get_param_or_400
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from app.models.address import Address


class AddressView(GenericViewSet):
    queryset = Address.objects.all()

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Address, 1)
        return serializer_class

    @action(methods=["get"],
            detail=False,
            url_path="findbyzip",
            schema=ManualSchema(description="Gets an address by zip code",
                                fields=[
                                    coreapi.Field(
                                        "zip",
                                        required=True,
                                        location="query",
                                        schema=coreschema.String(),
                                        description='Zip code')])
            )
    def find_address_by_zip(self, request: Request):
        zip_code = get_param_or_400(request.query_params, 'zip', str)

        if len(zip_code) != 8:
            raise ValueError(_("Zip code length should have exactly 8"))

        result_dict = {
            'city': {
                'id': None,
                'description': None
            },
            'zip': None,
            'neighborhood': {
                'id': None,
                'description': None
            },
            'state': {
                'id': None,
                'description': None,
                'initials': None
            },
            'address': None
        }

        try:
            address = Address.get_by_zip(zip_code)
        except Address.DoesNotExist:
            address = None

        if address:
            result_dict['city']['id'] = address.neighborhood.city.id
            result_dict['city']['description'] = address.neighborhood.city.description
            result_dict['zip'] = address.zip_code
            result_dict['neighborhood']['id'] = address.neighborhood.id
            result_dict['neighborhood']['description'] = address.neighborhood.description
            result_dict['state']['id'] = address.neighborhood.city.state.id
            result_dict['state']['description'] = address.neighborhood.city.state.description
            result_dict['state']['initials'] = address.neighborhood.city.state.initials
            result_dict['address'] = address.description

        return Response(data=result_dict)
