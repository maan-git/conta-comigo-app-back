from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from app.models.user import User
from simple_history.models import HistoricalRecords
from help.models.help_request_status import HelpRequestStatus
from help.models.help_category import HelpCategory


class HelpRequest (django_models.Model):
    owner_user = django_models.ForeignKey(User,
                                          on_delete=django_models.DO_NOTHING,
                                          related_name='help_requests')
    helping_users = django_models.ManyToManyField(User,
                                                  through="HelpRequestHelpers",
                                                  verbose_name=_("Users helping"),
                                                  related_name='helping_requests')
    description = django_models.TextField(_("Description"), db_index=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
    status = django_models.ForeignKey(HelpRequestStatus,
                                      verbose_name=_("Status"),
                                      on_delete=django_models.DO_NOTHING,
                                      related_name='help_requests',
                                      default=HelpRequestStatus.AllStatus.Created,
                                      db_index=True)
    category = django_models.ForeignKey(HelpCategory,
                                        verbose_name=_("Category"),
                                        on_delete=django_models.DO_NOTHING,
                                        related_name='help_requests',
                                        db_index=True)
    history = HistoricalRecords()



