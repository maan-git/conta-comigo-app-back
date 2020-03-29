from django.db import models as django_models
from simple_history.models import HistoricalRecords
from help.models.helping_status import HelpingStatus


class HelpRequestHelpers(django_models.Model):
    help_request = django_models.ForeignKey("HelpRequest", on_delete=django_models.CASCADE)
    helper_user = django_models.ForeignKey("app.User", on_delete=django_models.CASCADE)
    created = django_models.DateTimeField("Creation date", auto_now_add=True)
    status = django_models.ForeignKey(HelpingStatus,
                                      on_delete=django_models.CASCADE,
                                      default=HelpingStatus.AllStatus.Helping)
    history = HistoricalRecords()
