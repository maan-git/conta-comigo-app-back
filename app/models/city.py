from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from app.models.state import State


class City(django_models.Model):
    description = django_models.CharField(_("Description"), max_length=150)
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
    state = django_models.ForeignKey(State,
                                     verbose_name=_("State"),
                                     on_delete=django_models.DO_NOTHING,
                                     related_name='cities',
                                     db_index=True)


def import_from_external_source(external_address: dict) -> {City, None}:
    try:
        state = State.objects.get(initials=external_address.get('state_initials'))
    except State.DoesNotExist:
        # TODO log
        return None

    city_data = {'state': state, 'description': external_address.get('city_name')}
    city, create = City.objects.get_or_create(**city_data, defaults=city_data)

    return city
