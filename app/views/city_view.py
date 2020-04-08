from utils.views_utils import ModelViewSetReadOnly
from app.models.city import City
from utils.views_utils import get_generic_read_serializer


class CityView(ModelViewSetReadOnly):
    queryset = City.objects.all().select_related('state')
    filter_fields = {
        'state_id': ['exact']
    }

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(City, 1)
        return serializer_class
