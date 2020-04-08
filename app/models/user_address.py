from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from app.models.neighborhood import Neighborhood


class UserAddress(django_models.Model):
    neighborhood = django_models.ForeignKey(Neighborhood,
                                            verbose_name=_("Neighborhood"),
                                            on_delete=django_models.DO_NOTHING,
                                            related_name='user_addresses')
    address = django_models.CharField(_("Description"), max_length=150)
    zip_code = django_models.CharField(_("Zip code"), max_length=8)
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
