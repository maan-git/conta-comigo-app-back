from django.db import models


class EmailStatus(models.Model):
    class AllStatus:
        NOT_STARTED = 1
        SUCCESSFULLY_SEND = 2
        ERROR_SEND = 3

    id = models.IntegerField("Email status id", primary_key=True)
    description = models.CharField("Description", max_length=100)

    def __str__(self):
        return self.description
