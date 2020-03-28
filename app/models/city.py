from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class City(django_models.Model):
    name = django_models.CharField(
        _("City name"), max_length=50, null=False, blank=False
    )
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
