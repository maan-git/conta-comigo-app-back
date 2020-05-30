from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class GlobalVariableType(django_models.Model):
    class AllTypes:
        Integer = 1
        Date = 2
        DateTime = 3
        Float = 4
        Boolean = 5

    id = django_models.IntegerField(_("Description"), primary_key=True)
    description = django_models.CharField(_("Description"), max_length=200)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
