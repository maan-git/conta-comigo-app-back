from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from app.models.user import User
from simple_history.models import HistoricalRecords
from help.models.help_request_status import HelpRequestStatus
from help.models.help_category import HelpCategory
from help.models.help_request_cancel_reason import HelpRequestCancelReason
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError
from help.models.helping_status import HelpingStatus
from app.models.user_address import UserAddress


# Created → Canceled
# Created → In progress
# In progress → Created
# In progress → Canceled
# In progress → Canceled
allowed_status_changes = [
    {
        "from": HelpRequestStatus.AllStatus.Created,
        "to": HelpRequestStatus.AllStatus.Canceled,
    },
    {
        "from": HelpRequestStatus.AllStatus.Created,
        "to": HelpRequestStatus.AllStatus.InProgress,
    },
    {
        "from": HelpRequestStatus.AllStatus.InProgress,
        "to": HelpRequestStatus.AllStatus.Created,
    },
    {
        "from": HelpRequestStatus.AllStatus.InProgress,
        "to": HelpRequestStatus.AllStatus.Canceled,
    },
    {
        "from": HelpRequestStatus.AllStatus.InProgress,
        "to": HelpRequestStatus.AllStatus.Finished,
    },
]


class HelpRequest(django_models.Model):
    owner_user = django_models.ForeignKey(
        User, on_delete=django_models.DO_NOTHING, related_name="help_requests"
    )
    helping_users = django_models.ManyToManyField(
        User,
        through="HelpRequestHelpers",
        verbose_name=_("Users helping"),
        related_name="helping_requests",
    )
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
    cancel_reason = django_models.ForeignKey(HelpRequestCancelReason,
                                             verbose_name=_("Cancel reason"),
                                             on_delete=django_models.DO_NOTHING,
                                             related_name='help_requests',
                                             db_index=True,
                                             null=True,
                                             blank=True)
    address = django_models.ForeignKey(UserAddress,
                                       verbose_name=_("Address where the help request is needed"),
                                       on_delete=django_models.DO_NOTHING,
                                       related_name='help_requests',
                                       db_index=True)
    telephone_allowed = django_models.BooleanField(_("Telephone Allowed"))

    history = HistoricalRecords()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Saves original status id to use in the status change validation
        # In case of model loadings, the original status id will be the database persisted one
        self.original_status_id = self.status_id

    def check_status_change(self):
        if self.original_status_id and self.original_status_id != self.status_id:
            if self.is_status_final(self.original_status_id):
                raise ValidationError(
                    _("This help request was already in a final status")
                )
            else:
                allowed = any(
                    [
                        item
                        for item in allowed_status_changes
                        if item.get("from") == self.original_status_id
                        and item.get("to") == self.status_id
                    ]
                )

                if not allowed:
                    raise ValidationError(
                        _(
                            "Status change not allowed from {} to {}".format(
                                self.original_status_id, self.status_id
                            )
                        )
                    )

                if (
                    self.status_id == HelpRequestStatus.AllStatus.Canceled
                    and self.cancel_reason_id is None
                ):
                    raise ValidationError(_("Cancellations require a cancel reason"))

    @classmethod
    def is_status_final(cls, status_id: int):
        return status_id in [
            HelpRequestStatus.AllStatus.Canceled,
            HelpRequestStatus.AllStatus.Finished,
        ]

    @property
    def finished(self):
        return self.is_status_final(self.status_id)

    @property
    def any_user_helping(self):
        from help.models.helprequest_helpers import HelpRequestHelpers

        return HelpRequestHelpers.objects.filter(help_request=self, status_id=HelpingStatus.AllStatus.Helping).exists()


@receiver(pre_save, sender=HelpRequest)
def pre_save(sender, instance: HelpRequest, created=False, **kwargs):
    if not created:
        instance.check_status_change()
