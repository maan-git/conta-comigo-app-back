from django.db import models as django_models
from simple_history.models import HistoricalRecords
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Notification(django_models.Model):
    user = django_models.ForeignKey("User", on_delete=django_models.DO_NOTHING, related_name='notifications')
    email = django_models.ForeignKey("notification.Email", on_delete=django_models.CASCADE, null=True, blank=True)
    user_notification = django_models.ForeignKey("notification.UserNotification",
                                                 on_delete=django_models.CASCADE,
                                                 null=True,
                                                 blank=True)
    created = django_models.DateTimeField("Creation date", auto_now_add=True)
    notification_type = django_models.ForeignKey("NotificationType", on_delete=django_models.DO_NOTHING)
    history = HistoricalRecords()


@receiver(pre_save, sender=Notification)
def pre_save(sender, instance: Notification, created=False, **kwargs):
    if instance.email is None and instance.user_notification is None:
        raise ValidationError("It's not possible to create a notification with both email and user notification empty")
