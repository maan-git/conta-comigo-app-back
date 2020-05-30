from django.db.models import Lookup
from django.db import models as django_models
from django.db.models.fields import Field
from django.db.models import ForeignKey


class NotEqualLookup(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)

        params = [self.get_param_value(p) for p in lhs_params] + [self.get_param_value(p) for p in rhs_params]
        return '%s <> %s' % (lhs, rhs), params

    @classmethod
    def get_param_value(cls, param):
        if isinstance(param, django_models.Model):
            # TODO change to support other primary keys that are not named "id"
            return param.id
        else:
            return param

    @classmethod
    def register(cls):
        Field.register_lookup(NotEqualLookup)
        ForeignKey.register_lookup(NotEqualLookup)