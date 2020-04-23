from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class UserNotification(django_models.Model):
    content = django_models.TextField(_('Notification content'))

    def __str__(self) -> str:
        return self.content
