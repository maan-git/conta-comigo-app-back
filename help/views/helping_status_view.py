from help.models.helping_status import HelpingStatus
from utils.views_utils import get_generic_read_serializer
from utils.admin_edit_only_view import AdminEditOnlyViewNoDelete


class HelpingStatusView(AdminEditOnlyViewNoDelete):
    queryset = HelpingStatus.objects.all()
    ordering = ('description',)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(HelpingStatus, 0)
        return serializer_class
