from help.models.help_request_status import HelpRequestStatus
from utils.views_utils import get_generic_read_serializer
from utils.admin_edit_only_view import AdminEditOnlyView


class HelpRequestStatusView(AdminEditOnlyView):
    queryset = HelpRequestStatus.objects.all()
    ordering = ('description',)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(HelpRequestStatus, 0)
        return serializer_class