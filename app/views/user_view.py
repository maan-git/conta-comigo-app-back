import coreschema
import coreapi
from django.db import transaction
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from app.models.user import User
from app.serializers.user_serializer import UserSerializer
from app.serializers.user_serializer import UserSerializerPost
from app.serializers.user_serializer import UserSerializerCurrentUser
from app.serializers.user_serializer import UserNewPasswordSerializer
from utils.views_utils import ModelViewSetNoDelete
from utils.views_utils import get_param_or_400
from app.models.user_address import UserAddress
from utils.commom_utils import str_to_boolean
from app.serializers.user_address_serializer import UserAddressSerializer
from django_filters import rest_framework as filters

from app import generate_new_pass


class UserFilters(filters.FilterSet):
    neighborhood_id = filters.NumberFilter(field_name="addresses__neighborhood_id")
    city_id = filters.NumberFilter(field_name="addresses__neighborhood__city_id")
    state_id = filters.NumberFilter(field_name="addresses__neighborhood__city__state_id")

    class Meta:
        model = User
        fields = {
            'id': ['ne']
        }


class UserView(ModelViewSetNoDelete):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    filterset_class = UserFilters

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        else:
            return UserSerializerPost

    def get_permissions(self):
        """
       Instantiates and returns the list of permissions that this view requires.
       """
        if self.action == "create" or self.action == "reset_password":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(
        methods=["get"],
        detail=False,
        url_path="current",
        schema=ManualSchema(
            fields=[], description="Get the data from the currently logged user"
        ),
    )
    def get_current_user_data(self, request: Request):
        """
        Get the data from the currently logged user
        """
        return Response(data=UserSerializerCurrentUser(request.user).data)

    @action(
        methods=["get"],
        detail=True,
        url_path="getaddresses",
        schema=ManualSchema(
            description="Gets all addresses from a user",
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description="User ID",
                ),
                coreapi.Field(
                    "active",
                    required=False,
                    location="query",
                    schema=coreschema.Boolean(),
                    description="Active addresses",
                ),
            ],
        ),
    )
    def get_addresses(self, request: Request, pk: int):
        user = self.get_object()
        active = request.query_params.get("active", None)
        addresses_queryset = user.addresses.all().select_related(
            "neighborhood", "neighborhood__city", "neighborhood__city__state"
        )

        if active is not None:
            active = str_to_boolean(active)
            addresses_queryset = addresses_queryset.filter(active=active)

        return Response(data=UserAddressSerializer(addresses_queryset, many=True).data)

    @action(
        methods=["patch"],
        detail=True,
        url_path="changeaddressstatus",
        schema=ManualSchema(
            description="Updates the status of an address from the given user",
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description="User ID",
                ),
                coreapi.Field(
                    "address_id",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(),
                    description="Adress' ID",
                ),
                coreapi.Field(
                    "active",
                    required=False,
                    location="form",
                    schema=coreschema.Boolean(),
                    description="New value for the address' active attribute",
                ),
            ],
        ),
    )
    def change_address_status(self, request: Request, pk: int):
        user = self.get_object()
        address_id = get_param_or_400(request.data, "address_id", int)
        active = get_param_or_400(request.data, "active", bool)

        address = user.addresses.get(id=address_id)
        address.active = active
        address.save()

        return Response()

    @action(
        methods=["post"],
        detail=True,
        url_path="addaddress",
        schema=ManualSchema(
            description="Add a new addresses to the given user",
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description="User ID",
                ),
                coreapi.Field(
                    "neighborhood_id",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(),
                    description="Neighborhood' ID",
                ),
                coreapi.Field(
                    "address",
                    required=False,
                    location="form",
                    schema=coreschema.String(max_length=150),
                    description="State' ID",
                ),
                coreapi.Field(
                    "zip",
                    required=False,
                    location="form",
                    schema=coreschema.String(max_length=8),
                    description="ZIP code",
                ),
            ],
        ),
    )
    @transaction.atomic
    def add_address(self, request: Request, pk: int):
        user = self.get_object()
        neighborhood_id = get_param_or_400(request.data, "neighborhood_id", int)
        address = get_param_or_400(request.data, "address", str)
        zip_code = get_param_or_400(request.data, "zip", str)

        addresses_queryset = UserAddress.objects.all().select_related(
            "neighborhood", "neighborhood__city", "neighborhood__city__state"
        )
        new_address = addresses_queryset.create(
            neighborhood_id=neighborhood_id, address=address, zip_code=zip_code
        )
        user.addresses.add(new_address)
        user.save()

        return Response(data=UserAddressSerializer(new_address).data)

    @action(
        methods=["patch"],
        detail=True,
        url_path="updateaddress",
        schema=ManualSchema(
            description="Updates a user address",
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description="User ID",
                ),
                coreapi.Field(
                    "user_address_id",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(),
                    description="User address ID",
                ),
                coreapi.Field(
                    "neighborhood_id",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(),
                    description="Neighborhood' ID",
                ),
                coreapi.Field(
                    "address",
                    required=False,
                    location="form",
                    schema=coreschema.String(max_length=150),
                    description="State' ID",
                ),
                coreapi.Field(
                    "zip",
                    required=False,
                    location="form",
                    schema=coreschema.String(max_length=8),
                    description="ZIP code",
                ),
            ],
        ),
    )
    @transaction.atomic
    def update_address(self, request: Request, pk: int):
        user = self.get_object()
        address_id = get_param_or_400(request.data, "user_address_id", int)
        neighborhood_id = get_param_or_400(request.data, "neighborhood_id", int)
        address = get_param_or_400(request.data, "address", str)
        zip_code = get_param_or_400(request.data, "zip", str)

        user_address = user.addresses.get(id=address_id)
        user_address.neighborhood_id = neighborhood_id
        user_address.zip_code = zip_code
        user_address.address = address
        user_address.save()

        return Response()

    @action(
        methods=["post"],
        detail=False,
        url_path="resetpassword",
        schema=ManualSchema(
            description="User e-mail",
            fields=[
                coreapi.Field(
                    "email",
                    required=True,
                    location="form",
                    schema=coreschema.String(),
                    description="User e-mail",
                ),
            ],
        ),
    )
    @transaction.atomic
    def reset_password(self, request: Request):
        user = User.objects.all()
        email = get_param_or_400(request.data, "email", str)

        try:
            user_reset_pass = user.get(email=email)
            if user_reset_pass:
                new_pass = generate_new_pass(user_reset_pass)
                user_reset_pass.set_password(new_pass)
                user_reset_pass.save()

                email_render_data = {
                    'user': user_reset_pass.first_name,
                    'new_password': user_reset_pass
                }
                User.send_email('user_reset_password',
                                email_render_data,
                                'Conta Comigo APP - Recuperação de Senha')
                return Response(data=UserNewPasswordSerializer(user_reset_pass).data)

        except Exception as ex:
            raise ValueError(f"There is no register for {email}: {ex}")

        return Response()
