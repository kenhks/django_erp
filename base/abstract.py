from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class BaseAbstractModel(models.Model):
    """
    Abstract Base Model
    """
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created on'))
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        verbose_name=_('Created by'),
        related_name='create_%(app_label)s_%(class)s_set', editable=False)
    write_date = models.DateTimeField(
        auto_now=True, verbose_name=_('Last Modified on'))
    write_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        verbose_name=_('Last Modified by'),
        related_name='write_%(app_label)s_%(class)s_set', editable=False)

    class Meta:
        abstract = True

    def duplicate(self, user):
        """
        duplicate a new obj from this original object
        """
        self.pk = None
        self.create_user = self.write_user = user
        return self.save()


class ActiveControlMixin(models.Model):
    """
    A mixin model for model composition
    """
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    class Meta:
        abstract = True

    def disable(self, save=False):
        self.active = False
        if save:
            self.save()

    def enable(self, save=True):
        self.active = True
        if save:
            self.save()
