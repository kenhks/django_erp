from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class QmsConfig(AppConfig):
    name = 'qms'
    verbose_name = _('Quota Management')
