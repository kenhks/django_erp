from rest_framework import routers

from .viewsets import QuotaViewSet, QuotaAccountViewSet, QuotaTransactionViewSet, QuotaInventoryViewSet


api_router = routers.DefaultRouter()
api_router.register(r'quotas', QuotaViewSet, basename='quota')
api_router.register(r'quota_accounts', QuotaAccountViewSet, basename='quota_acocunt')
api_router.register(r'quota_transactions', QuotaTransactionViewSet, basename='quota_transaction')
api_router.register(r'quota_inventory', QuotaInventoryViewSet, basename='quota_inventory')

urlpatterns = api_router.urls
