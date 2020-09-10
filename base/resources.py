from import_export import resources

from .models import Company, User


class UserResource(resources.ModelResource):
    """
    Import/Export resource for model User
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class CompanyResource(resources.ModelResource):
    """
    Import/Export resource for model Company
    """
    class Meta:
        model = Company
        fields = ('id', 'name', 'parent__name',)
