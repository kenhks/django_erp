from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from base.admin import BaseAbstractModelAdmin, ViewOnlyAdminMixin
from .models import Quota, QuotaAccount, QuotaTransaction, QuotaInventory


@admin.register(Quota)
class QuotaAdmin(BaseAbstractModelAdmin):
    list_display = ('id', 'name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'description',),
        }),
    )


@admin.register(QuotaAccount)
class QuotaAccountAdmin(BaseAbstractModelAdmin):
    list_display = ('id', 'name', 'active', 'company')

    fieldsets = (
        (None, {
            'fields': ('name', 'active',),
        }),
        (None, {
            'fields': ('company', ),
        }),
    )


@admin.register(QuotaTransaction)
class QuotaTransactionAdmin(BaseAbstractModelAdmin):
    list_display = ('id', 'date', 'from_account', 'to_account', 'quota', 'quantity', )
    list_filter = ('date', )

    fieldsets = (
        (None, {
            'fields': ('date',),
        }),
        (_('Detail',), {
            'fields': ('from_account', 'to_account', 'quota', 'quantity', ),
        }),
    )

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(QuotaInventory)
class QuotaInventoryAdmin(ViewOnlyAdminMixin, admin.ModelAdmin):

    list_display = ('account', 'quota', 'quantity',)
