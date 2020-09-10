"""
Root API Views without any apps
"""
from django.conf import settings
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@cache_page(1440)
@api_view(http_method_names=['GET'])
@permission_classes(())
def version_view_get(request):
    return Response({'version': settings.VERSION})
