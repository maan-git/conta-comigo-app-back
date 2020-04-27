from django.db import models
from django.utils.translation import ugettext_lazy as _


class EmailStatus(models.Model):
    class AllStatus:
        WAITING = 1
        SUCCESSFULLY_SEND = 2
        ERROR_SEND = 3

    id = models.IntegerField(_("Email status id"), primary_key=True)
    description = models.CharField(_("Description"), max_length=100)

    def __str__(self):
        return self.description
