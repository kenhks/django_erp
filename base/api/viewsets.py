from rest_framework import viewsets

from ..models import Company, User
from .serializers import CompanySerializer, UserSerialzer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Company ModelViewSet
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User ModelViewSet
    """
    queryset = User.objects.all()
    serializer_class = UserSerialzer
