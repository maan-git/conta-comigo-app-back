from django.apps import AppConfig
from utils.queryset_lookups.not_equals import NotEqualLookup


class UtilsConfig(AppConfig):
    name = "utils"

    def ready(self):
        self._register_lookups()

    @classmethod
    def _register_lookups(cls):
        NotEqualLookup.register()
