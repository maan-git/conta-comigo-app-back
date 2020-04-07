import copy
import datetime
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.serializers import ModelSerializer
from . import commom_utils
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class GenericReadSerializer(ModelSerializer):
    class Meta:
        model = None
        depth = 1
        fields = "__all__"


class GenericWriteSerializer(ModelSerializer):
    class Meta:
        model = None
        depth = 0
        fields = "__all__"


def get_param_or_400(
    request_data: dict,
    param_name: str,
    parameter_type: type = None,
    default_value=None,
    integer_list: bool = False,
):
    if not param_name:
        return None

    param_value = request_data.get(param_name, None)

    if param_value is None:
        if default_value is None:
            raise ParseError(
                detail="The " + param_name + " parameter is required",
                code=status.HTTP_400_BAD_REQUEST,
            )
        else:
            return default_value

    try:
        if parameter_type is not None:
            if parameter_type == int:
                param_value = commom_utils.str_to_int(param_value, default_value)
            if parameter_type == float:
                param_value = commom_utils.str_to_float(param_value, default_value)
            if parameter_type == bool:
                param_value = commom_utils.str_to_boolean(
                    param_value, default_value
                )
            if parameter_type == list:
                param_value = param_value.split(",")
                if not isinstance(param_value, list):
                    param_value = list(param_value)
                if integer_list:
                    param_value = [int(v) for v in param_value]
            if parameter_type == datetime.date:
                param_value = commom_utils.str_to_date(param_value, default_value)
            if parameter_type == datetime.datetime:
                param_value = commom_utils.str_to_datetime(
                    param_value, default_value
                )
    except ValueError:
        raise ParseError(
            detail="The " + param_name + " value is not valid",
            code=status.HTTP_400_BAD_REQUEST,
        )

    return param_value


def get_generic_read_serializer(model: type, depth: int):
    """Get a copy of the generic read serializer."""
    serializer = copy.deepcopy(GenericReadSerializer)
    serializer.Meta.model = model
    serializer.Meta.depth = depth
    return serializer


def get_generic_write_serializer(model: type, depth: int):
    """Get a copy of the generic write serializer."""
    serializer = copy.deepcopy(GenericWriteSerializer)
    serializer.Meta.model = model
    serializer.Meta.depth = depth
    return serializer


class ModelViewSetNoDelete(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()` and `list()` actions.
    """
    pass


class ModelViewSetReadOnly(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `retrieve()` and `list()` actions.
    """
    pass
