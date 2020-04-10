import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from validate_docbr import CPF
import phonenumbers


def validate_phone(value):
    if not phonenumbers.is_valid_number(phonenumbers.parse(value, 'BR')):
        raise ValidationError(
            _('%(value)s is not a valid phone number'),
            params={'value': value},
        )


def validate_cpf(value):
    cpf = CPF()

    try:
        valid = cpf.validate(value)
    except:
        valid = False

    if not valid:
        raise ValidationError(
            _('%(value)s is not a valid CPF'),
            params={'value': value},
        )
