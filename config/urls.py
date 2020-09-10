"""
Project django_erp URL Configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import version_view_get

token_urls = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

api_urls = [
    *token_urls,
    path('version/', version_view_get, name='version'),
    path('schema', get_schema_view(title='ERP API')),
    path('docs/', include_docs_urls(title='API Docs',
                                    permission_classes=(AllowAny,)
                                    )),
    path('', RedirectView.as_view(url='docs/', permanent=False), name='api'),
    path('base/', include('base.api.urls')),
    path('qms/', include('qms.api.urls')),
]

app_urls = [

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('silk/', include('silk.urls', namespace='silk')),
    path('accounts/', include('allauth.urls')),
    path(f'{settings.API_URL}', include(api_urls)),
    *app_urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
