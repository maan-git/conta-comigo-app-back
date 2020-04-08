from django.db import models as django_models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from app.models.global_variable_type import GlobalVariableType
from django.utils.translation import ugettext_lazy as _
from utils import commom_utils


class GlobalVariable(django_models.Model):
    id = django_models.IntegerField(_('ID'), primary_key=True)
    key = django_models.CharField("Key", max_length=100, null=False, unique=True)
    description = django_models.CharField(_("Description"), max_length=200)
    value = django_models.TextField(_("Global variable value"), null=True, blank=True)
    created = django_models.DateTimeField(_("Creation date"), auto_now_add=True)
    type = django_models.ForeignKey(GlobalVariableType,
                                    verbose_name=_("Global variable"),
                                    on_delete=django_models.DO_NOTHING,
                                    related_name='global_variables')

    @property
    def converted_value(self):
        if not self.value:
            return None

        if self.type_id == GlobalVariableType.AllTypes.Integer:
            return commom_utils.str_to_int(self.value, None)

        elif self.type_id == GlobalVariableType.AllTypes.Date:
            return commom_utils.str_to_date(self.value, None)

        elif self.type_id == GlobalVariableType.AllTypes.DateTime:
            return commom_utils.str_to_datetime(self.value, None)

        elif self.type_id == GlobalVariableType.AllTypes.Float:
            return commom_utils.str_to_float(self.value, None)

        elif self.type_id == GlobalVariableType.AllTypes.Boolean:
            return commom_utils.str_to_boolean(self.value, None)

    @classmethod
    def serialize_value(cls, var_type: GlobalVariableType, var_value):
        if var_value is None:
            return None

        if var_type.id == GlobalVariableType.AllTypes.Integer:
            return commom_utils.int_to_str(var_value)

        elif var_type.id == GlobalVariableType.AllTypes.Date:
            return commom_utils.date_to_str(var_value)

        elif var_type.id == GlobalVariableType.AllTypes.DateTime:
            return commom_utils.datetime_to_str(var_value)

        elif var_type.id == GlobalVariableType.AllTypes.Float:
            return commom_utils.float_to_str(var_value)

        elif var_type.id == GlobalVariableType.AllTypes.Boolean:
            return commom_utils.boolean_to_str(var_value)

    def __str__(self):
        return self.key


def get_global_variable_value(key: str, default: str = None) -> str:
    """Get the current value of a global variable by its key"""
    try:
        variable = GlobalVariable.objects.get(key=key)
        return variable.converted_value
    except:
        return default


def update_global_variable_value(key, new_value):
    """Update the current value of a global variable by its key"""
    variable = GlobalVariable.objects.get(key=key)
    variable.value = GlobalVariable.serialize_value(variable.type, new_value)
    variable.save()


@receiver(pre_save, sender=GlobalVariable)
def pre_save(sender, instance: GlobalVariable, created=False, raw=False, **kwargs):
    if raw:
        # It's a fixture load doing an update. Don't change the value
        try:
            saved_value = GlobalVariable.objects.get(id=instance.id).value
            exists = True
        except GlobalVariable.DoesNotExist:
            saved_value = ''
            exists = False

        if exists and saved_value != instance.value:
            instance.value = saved_value
