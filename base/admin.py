from django.contrib import admin, messages
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin,
    GroupAdmin as BaseGroupAdmin
)
from django.contrib.auth.models import Group as BaseGroup
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin

from .models import User, Company, Group
from .resources import CompanyResource, UserResource
# from .admin_extra import *

admin.site.unregister(BaseGroup)


class BaseAbstractModelAdmin(admin.ModelAdmin):
    """
    Abstract admin class for any model inherited BaseAbstractModel
    """
    superuser_fields = ('create_date', 'create_user',
                        'write_date', 'write_user')
    superuser_fieldsets = (
        (_('Meta'), {
            'fields': (
                ('create_date', 'create_user'),
                ('write_date', 'write_user'),
            )
        }),
    )
    actions = ['duplicate_queryset']

    def duplicate_queryset(self, request, queryset):
        """Given a queryset, duplicate it from the database."""
        success = False
        with transaction.atomic():
            for record in queryset:
                record.duplicate(request.user)
            success = True
        if success:
            self.message_user(request, _('Successfully copied {}').format(
                len(queryset)), messages.SUCCESS)
        else:
            self.message_user(request, _('Failed to copy {}').format(
                len(queryset)), messages.ERROR)
    duplicate_queryset.short_description = 'Duplicate'
    duplicate_queryset.allowed_permissions = ('add',)

    def get_fields(self, request, obj):
        raise AttributeError(_('Please use fieldsets instead of fields'))

    def get_fieldsets(self, request, obj=None):
        res = super().get_fieldsets(request, obj)
        if obj and request.user.is_superuser:
            return res + self.superuser_fieldsets
        else:
            return res

    def get_list_display(self, request):
        res = super().get_list_display(request)
        if request.user.is_superuser:
            return res + self.superuser_fields
        else:
            return res

    def get_list_filter(self, request):
        res = super().get_list_filter(request)
        if request.user.is_superuser:
            return res + self.superuser_fields
        else:
            return res

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + self.superuser_fields

    def save_model(self, request, obj, form, change):
        if change:
            obj.write_user = request.user
        else:
            obj.create_user = obj.write_user = request.user
        super().save_model(request, obj, form, change)


class ViewOnlyAdminMixin:
    """
    Admin Mixin that allow read-only access on model
    regardless of the user permissions
    """

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Company)
class CompanyAdmin(ImportExportMixin, BaseAbstractModelAdmin):
    """
    Admin for model Company
    """
    # List View Parameter
    resource_class = CompanyResource
    list_display = ('id', 'name',)
    list_per_page = 10
    search_fields = ('name',)
    # Form View Parameter
    fieldsets = (
        (None, {
            'fields': ('name', 'parent')
        }),
        (_('Tree Infomation', ), {
            'fields': (
                ('tree_id', 'level',),
                ('lft', 'rght',),
            )
        }),
    )
    readonly_fields = ('tree_id', 'level', 'lft', 'rght', )


@admin.register(User)
class UserAdmin(ImportExportMixin, BaseUserAdmin, BaseAbstractModelAdmin):
    """
    Admin for model User
    """
    # List View Parameter
    resource_class = UserResource
    list_display = ('id', 'username', 'email', 'is_staff',)
    readonly_fields = ('last_login', 'date_joined',)
    company_fieldsets = (
        (_('Company Access'), {
            'fields': ('companies',),
        }),
    )
    filter_horizontal = ('companies',)

    def get_fieldsets(self, request, obj=None):
        return super().get_fieldsets(request, obj) + self.company_fieldsets


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin):
    pass
