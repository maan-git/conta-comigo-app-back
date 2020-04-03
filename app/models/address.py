from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class Address(django_models.Model):
    adress = django_models.CharField(
        _("Address"), max_length=250, null=False, blank=False
    )
    complement = django_models.CharField(
        _("Complement"), max_length=80, null=False, blank=False
    )
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
