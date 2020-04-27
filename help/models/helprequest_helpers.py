from django.db import models as django_models
from simple_history.models import HistoricalRecords
from help.models.helping_status import HelpingStatus
from django.db.models.signals import post_save
from django.dispatch import receiver
from help.models.help_request_status import HelpRequestStatus
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from app.models.notification_type import NotificationType


class HelpRequestHelpers(django_models.Model):
    help_request = django_models.ForeignKey("HelpRequest", on_delete=django_models.CASCADE)
    helper_user = django_models.ForeignKey("app.User", on_delete=django_models.CASCADE)
    created = django_models.DateTimeField("Creation date", auto_now_add=True)
    status = django_models.ForeignKey(HelpingStatus,
                                      on_delete=django_models.CASCADE,
                                      default=HelpingStatus.AllStatus.Helping)
    history = HistoricalRecords()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_status_id = self.status_id

    def notify_help_request_owner_status(self):
        if self.status_id == HelpingStatus.AllStatus.Helping:
            email_subject = _('User applied to help')
            notification_type = NotificationType.AllTypes.USER_APPLIED_TO_HELP
            notification_message = ugettext('User {} applied to help in request {}'
                                            .format(self.helper_user.first_name, self.help_request.description))
            email_template_name = 'user_applied_to_help.html'
        else:
            email_subject = _('User unapplied to help')
            notification_type = NotificationType.AllTypes.USER_UNAPPLIED_FROM_HELP
            notification_message = ugettext('User {} unapplied to help in request {}'
                                     .format(self.helper_user.first_name, self.help_request.description))
            email_template_name = 'user_unapplied_from_help.html'

        email_render_data = {
            'user': self.help_request.owner_user.first_name,
            'applied_user': self.helper_user.first_name,
            'help_request': self.help_request.description
        }

        self.help_request.owner_user.notify(notification_type,
                                            notification_message,
                                            f'emails/{email_template_name}',
                                            email_render_data,
                                            email_subject)


@receiver(post_save, sender=HelpRequestHelpers)
def post_save(sender, instance: HelpRequestHelpers, created=False, **kwargs):
    if created or (instance.status_id != instance.original_status_id):
        instance.notify_help_request_owner_status()
