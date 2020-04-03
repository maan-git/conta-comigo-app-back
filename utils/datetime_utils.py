import calendar
from django.conf import settings
from datetime import timedelta
from datetime import datetime
from datetime import date


def datetime_to_timestamp(date_time: datetime):
    """Converts a date/datetime to unix timestamp"""
    return calendar.timegm(date_time.timetuple())


def subtract_days(dt, days: int):
    return dt - timedelta(days=days)


def add_days(dt, days: int):
    return dt + timedelta(days=days)


def get_date(year: int, month: int, day: int):
    return datetime(year=year, month=month, day=day)


def str_to_date(
    string_to_convert: str, formats: dict = None, default_value: date = None
):
    return _convert_str(
        string_to_convert, True, formats=formats, default_value=default_value
    )


def str_to_datetime(
    string_to_convert: str, formats: dict = None, default_value: datetime = None
):
    return _convert_str(
        string_to_convert, False, formats=formats, default_value=default_value
    )


def _convert_str(
    string_to_convert: str, to_date: bool, formats: dict = None, default_value=None
):
    if not formats:
        formats = list(settings.REST_FRAMEWORK.get("DATE_INPUT_FORMATS"))
        if not to_date:
            # Datetime accepts the date formats too
            formats.extend(settings.REST_FRAMEWORK.get("DATETIME_INPUT_FORMATS"))

    if formats is None:
        return None

    for f in formats:
        try:
            converted_datetime = datetime.strptime(string_to_convert, f)
            if to_date:
                return converted_datetime.date()
            else:
                return converted_datetime
        except ValueError:
            pass

    if default_value is not None:
        return default_value
    else:
        error = ValueError(string_to_convert)
        if not error.args:
            error.args = ("",)

        error.args = error.args + (
            "The value is not valid for any of the formats " + formats,
        )
        raise error.args


def diff_in_months(start_date, end_date):
    return (start_date.year - end_date.year) * 12 + start_date.month - end_date.month
