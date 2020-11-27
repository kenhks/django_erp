from django.contrib import admin
from .models import Organization, OrganizationMember, OrganizationMemberRole

class OrganizationMemberInline(admin.TabularInline):
    model = Organization.users.through
    extra = 0

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    # List View Parameter
    list_display = ("id", "name", "level", "create_date", "write_date")
    list_editable = ("name", "level")
    list_per_page = 50
    list_filter = ("level", "create_date", "write_date", )
    ordering = ("level", "name",)
    search_fields = ("name", "create_date",)
    # Form View Parameter
    fields = (
        ("name", ),
        ("parent", "level"),
    )
    inlines = [OrganizationMemberInline, ]


@admin.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "organization_id", "user_id", )

@admin.register(OrganizationMemberRole)
class OrganizationMemberRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)

