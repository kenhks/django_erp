from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BaseConfig(AppConfig):
    """
    App Configuration for base
    """
    name = 'base'
    verbose_name = _('Settings')
