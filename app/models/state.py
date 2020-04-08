from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class State(django_models.Model):
    id = django_models.IntegerField(_('ID'), primary_key=True)
    description = django_models.CharField(_("Description"), max_length=50)
    initials = django_models.CharField(_("Initials"), max_length=2, unique=True)
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)


