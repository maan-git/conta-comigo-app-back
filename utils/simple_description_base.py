from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class SimpleDescriptionBase(django_models.Model):
    class Meta:
        abstract = True

    description = django_models.CharField(
        _("Description"), max_length=50, null=False, blank=False
    )
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)


class SimpleDescriptionBaseWithId(SimpleDescriptionBase):
    class Meta:
        abstract = True

    id = django_models.IntegerField(_("ID"), primary_key=True)
