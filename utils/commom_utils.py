import datetime
import re
import os
from django.template import loader
from . import datetime_utils
from rest_framework.settings import ISO_8601


def str_to_int(value, default_value: int = None):
    try:
        converted_value = int(value)
    except ValueError:
        if default_value is not None:
            raise
        else:
            converted_value = default_value

    return converted_value


def int_to_str(value: int) -> str:
    return str(value)


def str_to_float(value, default_value: float = None):
    try:
        converted_value = float(value)
    except ValueError:
        if default_value is None:
            raise
        else:
            converted_value = default_value

    return converted_value


def float_to_str(value: float) -> str:
    return str(value)


def str_to_datetime(value, default_value: datetime.datetime = None):
    return datetime_utils.str_to_datetime(value, default_value=default_value)


def datetime_to_str(value: datetime.datetime) -> str:
    return value.isoformat()


def str_to_date(value, default_value: datetime.date = None):
    return datetime_utils.str_to_date(value, default_value=default_value)


def date_to_str(value: datetime.date) -> str:
    return value.strftime("%Y/%m/%d")


def str_to_boolean(value, default_value: bool = None):
    if value is None:
        return default_value

    if isinstance(value, bool):
        return value

    return value.upper().strip() == "TRUE"


def boolean_to_str(value: bool) -> str:
    return "True" if value else "False"


def get_package_version(package_name):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package_name, "__init__.py")).read()
    return re.match("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def render_template(template_name: str, context: dict):
    """Render a template with a dictionary data."""
    t = loader.get_template(template_name)
    return t.render(context)
