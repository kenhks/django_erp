from django.contrib.auth.models import (
    AbstractUser,
    Group as BaseGroup
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from .abstract import BaseAbstractModel


class Group(BaseGroup):
    """
    A Fake Proxy Group to change app label for group
    """
    class Meta:
        proxy = True
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class User(AbstractUser, BaseAbstractModel):
    """
    Users within the Django authentication system are represented by this
    model.
    Customized user model for project
    Username and password are required. Other fields are optional.
    """
    companies = models.ManyToManyField(
        'base.company',
        blank=True,
        verbose_name=_('Allowed Companies'),
        help_text=_(
            'The companies this user belongs to. A user will get all accesses '
            'granted to each of their companies.'
        ),
        related_name='users',
        related_query_name='user',
    )

    class Meta(AbstractUser.Meta):
        abstract = False
        ordering = ['-id']

    @property
    def get_all_permissions_sorted(self):
        return sorted(self.get_all_permissions())


class Company(MPTTModel, BaseAbstractModel):
    """
    Records are stricted access by company which is represented by this model.
    This model use MPTT for data hierarchy.
    """
    name = models.CharField(verbose_name=_('Name'), max_length=255,
                            null=False, unique=True,
                            help_text=_('A unique string to name this company'),)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, related_name='children',
                            null=True, blank=True,
                            verbose_name=_('Parent Company'),
                            help_text=_('The company owned this company'),)

    class Meta:
        ordering = ['-id']
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name

    def duplicate(self, user):
        self.name += _('(copy)')
        return super().duplicate(user)
