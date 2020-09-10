from rest_framework import serializers

from ..models import Company, User


class AbstractModelSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        if self.context.get('request') and hasattr(self.context.get('request'), 'user'):
            user = self.context['request'].user
            if user.is_authenticated:
                kwargs.setdefault('write_user', self.context['request'].user)
                kwargs.setdefault('create_user', self.context['request'].user)
        return super().save(**kwargs)


class CompanySerializer(AbstractModelSerializer):
    """
    Model Serializer for model Company
    """
    class Meta:
        model = Company
        fields = ('id', 'name', 'parent', 'create_date',
                  'create_user', 'write_date', 'write_user')
        # read_only_fields = ('id', 'create_date', 'create_user', 'write_date', 'write_user')


class UserSerialzer(AbstractModelSerializer):
    """
    Model Serializer for model User
    """
    permissions = serializers.ListField(
        child=serializers.CharField(), source='get_all_permissions_sorted',
        required=False, read_only=True,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active',
                  'date_joined', 'permissions')
        read_only_fields = ('id', 'is_active', 'date_joined')
