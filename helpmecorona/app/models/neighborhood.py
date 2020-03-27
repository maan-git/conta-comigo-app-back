from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class Neighborhood (django_models.Model):
    neighborhood = django_models.CharField(_("Neighborhood"), max_length=150, null=False, blank=False)
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
