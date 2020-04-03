from rest_framework.viewsets import ModelViewSet
from app.models.neighborhood import Neighborhood
from utils.views_utils import get_generic_read_serializer


class NeighborhoodView(ModelViewSet):
    queryset = Neighborhood.objects.all()
    ordering = ("name",)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Neighborhood, 1)
        return serializer_class
