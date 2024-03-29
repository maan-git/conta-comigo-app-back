from help.models.help_request_cancel_reason import HelpRequestCancelReason
from utils.views_utils import get_generic_read_serializer
from utils.admin_edit_only_view import AdminEditOnlyViewNoDelete


class HelpRequestCancelReasonView(AdminEditOnlyViewNoDelete):
    queryset = HelpRequestCancelReason.objects.all()
    ordering = ("description",)

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(HelpRequestCancelReason, 0)
        return serializer_class
