from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _


class HelpCategory(django_models.Model):
    id = django_models.IntegerField(primary_key=True)
    name = django_models.CharField(
        _("Category name"), max_length=50, null=False, blank=False
    )
    active = django_models.BooleanField(_("Active"), default=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
