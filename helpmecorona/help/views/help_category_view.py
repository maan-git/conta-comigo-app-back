from rest_framework.viewsets import ModelViewSet
from help.models.help_category import HelpCategory
from utils.views_utils import get_generic_read_serializer


class HelpCategoryView(ModelViewSet):
    queryset = HelpCategory.objects.all()
    ordering = ('name',)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(HelpCategory, 1)
        return serializer_class
