from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from utils.simple_description_base import SimpleDescriptionBaseWithId


class HelpingStatus(SimpleDescriptionBaseWithId):
    class AllStatus:
        Helping = 1
        Canceled = 100
