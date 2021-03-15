from rest_framework import viewsets, permissions
from .models import Premises, Premises_types, Rates, Additional_services
from .serializers import PremisesSerializer, PremisesTypesSerializer, RatesSerializer, AdditionalServicesSerializer

class PremisesViewSet (viewsets.ModelViewSet):
    queryset = Premises.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PremisesSerializer

class PremisesTypesViewSet (viewsets.ModelViewSet):
    queryset = Premises_types.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PremisesTypesSerializer

class RatesViewSet (viewsets.ModelViewSet):
    queryset = Rates.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RatesSerializer

class AdditionalServicesViewSet (viewsets.ModelViewSet):
    queryset = Additional_services.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AdditionalServicesSerializer
