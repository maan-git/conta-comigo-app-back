from django.db import models as django_models
from simple_history.models import HistoricalRecords
from help.models.helping_status import HelpingStatus
from django.db.models.signals import post_save
from django.dispatch import receiver
from help.models.help_request_status import HelpRequestStatus


class HelpRequestHelpers(django_models.Model):
    help_request = django_models.ForeignKey(
        "HelpRequest", on_delete=django_models.CASCADE
    )
    helper_user = django_models.ForeignKey("app.User", on_delete=django_models.CASCADE)
    created = django_models.DateTimeField("Creation date", auto_now_add=True)
    status = django_models.ForeignKey(
        HelpingStatus,
        on_delete=django_models.CASCADE,
        default=HelpingStatus.AllStatus.Helping,
    )
    history = HistoricalRecords()


@receiver(post_save, sender=HelpRequestHelpers)
def post_save(sender, instance: HelpRequestHelpers, created=False, **kwargs):
    if instance.help_request.any_user_helping:
        instance.help_request.status_id = HelpRequestStatus.AllStatus.InProgress
    else:
        instance.help_request.status_id = HelpRequestStatus.AllStatus.Created

    instance.help_request.save()
