# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _

class BaseAbstractModel(models.Model):
    """
    Abstract Base Model
    """
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created on"))
    write_date = models.DateTimeField(auto_now=True, verbose_name=_("Last Modified on"))

    class Meta:
        abstract = True
        get_latest_by = "write_date"

class ActiveControlMixin(models.Model):
    """
    A mixin model for model composition
    """
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class OrganizationMixin(models.Model):
    """
    A abstract mixin to transform normal model to oraganization-aware model
    """
    organization = models.ManyToManyField("Organization",
                                          related_name="orgs", related_query_name="org")

    class Meta:
        abstract = True
