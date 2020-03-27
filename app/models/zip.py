from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class Zip (django_models.Model):
    zip = django_models.CharField(_("Zip code"), max_length=12, null=False, blank=False)
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
