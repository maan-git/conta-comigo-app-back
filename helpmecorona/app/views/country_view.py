from rest_framework.viewsets import ModelViewSet
from app.models.country import Country
from utils.views_utils import get_generic_read_serializer


class CountryView(ModelViewSet):
    queryset = Country.objects.all()
    ordering = ('name',)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(Country, 1)
        return serializer_class
