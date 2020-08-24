# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class BaseAbstractModel(models.Model):
    """
    Abstract Base Model
    """
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created on"))
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name=_("Created by"))
    write_date = models.DateTimeField(
        auto_now=True, verbose_name=_("Last Modified on"))
    write_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name=_("Last Modified by"))

    class Meta:
        abstract = True
        get_latest_by = "write_date"


class ActiveControlMixin(models.Model):
    """
    A mixin model for model composition
    """
    active = models.BooleanField(default=True, verbose_name=_("Active"))

    class Meta:
        abstract = True

    def disable(self, save=False):
        self.active = False
        if save:
            self.save()


class OrganizationMixin(models.Model):
    """
    A abstract mixin to transform normal model to oraganization-aware model
    """
    organization = models.ManyToManyField("Organization",
                                          related_name="orgs", related_query_name="org")

    class Meta:
        abstract = True
