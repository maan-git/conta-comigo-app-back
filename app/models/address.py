from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from app.models.neighborhood import Neighborhood
from django.conf import settings
from app.models.neighborhood import import_from_external_source as import_external_neighborhood


external_provider_class = settings.EXTERNAL_ADDRESS_PROVIDER


class Address(django_models.Model):
    description = django_models.CharField(_("Description"), max_length=150)
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
    zip_code = django_models.CharField(_("Zip code"), max_length=8)
    neighborhood = django_models.ForeignKey(Neighborhood,
                                            verbose_name=_("Neighborhood"),
                                            on_delete=django_models.DO_NOTHING,
                                            related_name='addresses',
                                            db_index=True)

    @classmethod
    def get_by_zip(cls, zip_code: str):
        try:
            app_address = Address.objects.get(zip_code=zip_code)
        except Address.DoesNotExist:
            app_address = None

        if app_address is None:
            external_provider = external_provider_class()
            external_result = external_provider.get_address_by_zip(zip_code)

            if external_result is not None:
                app_address = import_from_external_source(external_result)

        return app_address


def import_from_external_source(external_address: dict) -> {Address, None}:
    neighborhood = import_external_neighborhood(external_address)

    if neighborhood is None:
        return None

    address_data = {'neighborhood': neighborhood,
                    'description': external_address.get('address'),
                    'zip_code': external_address.get('zip')}
    address, create = Address.objects.get_or_create(**address_data, defaults=address_data)

    return address
