from rest_framework import routers

from .viewsets import CompanyViewSet, UserViewSet

app_name = "base"
app_api_router = routers.DefaultRouter()
app_api_router.register(r'users', UserViewSet, basename='user')
app_api_router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = app_api_router.urls
