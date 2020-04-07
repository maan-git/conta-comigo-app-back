from utils.views_utils import ModelViewSetReadOnly
from app.models.neighborhood import Neighborhood
from utils.views_utils import get_generic_read_serializer


class NeighborhoodView(ModelViewSetReadOnly):
    queryset = Neighborhood.objects.all()

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Neighborhood, 1)
        return serializer_class
