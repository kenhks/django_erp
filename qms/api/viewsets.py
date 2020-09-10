from rest_framework import viewsets
from ..models import Quota, QuotaAccount, QuotaTransaction, QuotaInventory
from .serializers import QuotaSerializer, QuotaAccountSerializer, QuotaTransactionSerializer, QuotaInventorySerializer


class QuotaViewSet(viewsets.ModelViewSet):
    """
    Quota ModelViewSet
    """
    queryset = Quota.objects.all()
    serializer_class = QuotaSerializer


class QuotaAccountViewSet(viewsets.ModelViewSet):
    """
    QuotaAccount ModelViewSet
    """
    queryset = QuotaAccount.objects.all()
    serializer_class = QuotaAccountSerializer


class QuotaTransactionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    QuotaTransaction Readonly ModelViewset
    """
    queryset = QuotaTransaction.objects.all()
    serializer_class = QuotaTransactionSerializer


class QuotaInventoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    QuotaInventory ModelViewset
    """
    queryset = QuotaInventory.objects.all()
    serializer_class = QuotaInventorySerializer
