from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from cuser.models import CUser


class User (CUser):
    pass
