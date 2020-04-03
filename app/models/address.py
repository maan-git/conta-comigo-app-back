from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class Address(django_models.Model):
    adress = django_models.CharField(
        _("Address"), max_length=250, null=False, blank=False
    )
    zip = django_models.CharField(_("Zip code"), max_length=12, null=False, blank=False)
    city_name = django_models.CharField(
        _("City name"), max_length=50, null=False, blank=False
    )
    country_name = django_models.CharField(
        _("Country name"), max_length=50, null=False, blank=False
    )
    neighborhood = django_models.CharField(
        _("Neighborhood"), max_length=150, null=False, blank=False
    )
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
