from rest_framework.serializers import ModelSerializer
from base.api.serializers import AbstractModelSerializer
from ..models import Quota, QuotaAccount, QuotaTransaction, QuotaInventory

class QuotaSerializer(AbstractModelSerializer):
    """
    Model Serializer for model Quota
    """
    class Meta:
        model = Quota
        fields = "__all__"

class QuotaAccountSerializer(AbstractModelSerializer):
    """
    Model Serializer for model QuotaAccount
    """
    class Meta:
        model = QuotaAccount
        fields = "__all__"

class QuotaTransactionSerializer(AbstractModelSerializer):
    """
    Model Serializer for model QuotaTransaction
    """
    class Meta:
        model = QuotaTransaction
        fields = "__all__"

class QuotaInventorySerializer(ModelSerializer):
    """
    Model Serializer for model QuotaTransaction
    """
    class Meta:
        model = QuotaInventory
        fields = "__all__"
