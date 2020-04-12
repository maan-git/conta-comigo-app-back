from utils.views_utils import ModelViewSetReadOnly
from app.models.neighborhood import Neighborhood
from utils.views_utils import get_generic_read_serializer

from rest_framework.permissions import AllowAny


class NeighborhoodView(ModelViewSetReadOnly):
    permission_classes = (AllowAny,)
    queryset = Neighborhood.objects.all().select_related("city", "city__state")
    filter_fields = {"city__state_id": ["exact"], "city_id": ["exact"]}

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Neighborhood, 1)
        return serializer_class
