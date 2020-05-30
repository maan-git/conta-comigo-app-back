from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from app.models.city import City
from app.models.city import import_from_external_source as import_city_external


class Neighborhood(django_models.Model):
    description = django_models.CharField(_("Description"), max_length=150)
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
    city = django_models.ForeignKey(
        City,
        verbose_name=_("City"),
        on_delete=django_models.DO_NOTHING,
        related_name="neighborhoods",
        db_index=True,
    )


def import_from_external_source(external_address: dict) -> {Neighborhood, None}:
    city = import_city_external(external_address)

    if city is None:
        return None

    neighborhood_data = {
        "city": city,
        "description": external_address.get("neighborhood_name"),
    }
    neighborhood, create = Neighborhood.objects.get_or_create(
        **neighborhood_data, defaults=neighborhood_data
    )

    return neighborhood
