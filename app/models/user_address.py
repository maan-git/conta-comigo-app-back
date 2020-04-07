from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from app.models.address import Address
from app.models.user import User


class UserAddress(django_models.Model):
    user_address = django_models.ForeignKey(User,
                                            on_delete=django_models.DO_NOTHING,
                                            related_name='user_address')
    addres = django_models.ForeignKey(Address,
                                      on_delete=django_models.DO_NOTHING,
                                      related_name='address')
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
