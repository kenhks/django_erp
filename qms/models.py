import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.abstract import BaseAbstractModel


class Quota(BaseAbstractModel):

    name = models.CharField(verbose_name=_('Name'), max_length=255,
                            null=False, unique=True,
                            help_text=_('A unique string to name this quota type'),)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True,
                                   help_text=_('Detail explanation for this quota'),)
    company = models.ForeignKey('base.Company', verbose_name=_('Company'), on_delete=models.PROTECT,
                                help_text=_('Company who own this quota type'),
                                null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Quota')

    def __str__(self):
        return self.name


class QuotaAccount(BaseAbstractModel):

    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_('Name'),
                            help_text=_('A unique string to name this quota'),)
    active = models.BooleanField(verbose_name=_('Active'), default=True,
                                 help_text=_('You can disable a account without deleting it'),)
    company = models.ForeignKey('base.Company', verbose_name=_('Company'),
                                on_delete=models.PROTECT, null=True, blank=True,
                                help_text=_('Company who own this account'),
                                )

    class Meta:
        ordering = ['-id']
        verbose_name = _('Quota Account')

    def __str__(self):
        return self.name


class QuotaTransaction(BaseAbstractModel):
    date = models.DateTimeField(
        default=datetime.datetime.now, verbose_name=_('Date'))
    from_account = models.ForeignKey('QuotaAccount',
                                     on_delete=models.PROTECT,
                                     related_name='outgoing_trans',
                                     verbose_name=_('From Account'))
    to_account = models.ForeignKey('QuotaAccount',
                                   on_delete=models.PROTECT,
                                   related_name='incoming_trans',
                                   verbose_name=_('To Account'))
    quota = models.ForeignKey('Quota', on_delete=models.PROTECT,
                              verbose_name=_('Quota'))
    quantity = models.PositiveIntegerField(default=1,
                                           verbose_name=_('Quantity'),)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Quota Transaction')


class QuotaInventory(models.Model):

    account = models.ForeignKey(QuotaAccount, on_delete=models.CASCADE,
                                verbose_name=_('Quota Account'), related_name="inventory")
    quota = models.ForeignKey(Quota, on_delete=models.CASCADE,
                              verbose_name=_('Quota'),)
    quantity = models.IntegerField(default=0)

    class Meta:
        managed = False
        ordering = ['account', 'quota', ]
        db_table = 'qms_quotainventory'
        verbose_name = _('Report - Inventory')
        verbose_name_plural = _('Report - Inventory')
