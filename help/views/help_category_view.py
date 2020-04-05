from help.models.help_category import HelpCategory
from utils.views_utils import get_generic_read_serializer
from utils.admin_edit_only_view import AdminEditOnlyViewNoDelete


class HelpCategoryView(AdminEditOnlyViewNoDelete):
    queryset = HelpCategory.objects.all()
    ordering = ('description',)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(HelpCategory, 0)
        return serializer_class
