from rest_framework import viewsets, permissions
from .models import Tenants, Individuals, Entits, Individual_entrepreneurs, Discount_cards, Deals
from .serializers import TenantsrSerializer, IndividualsSerializer, EntitsSerializer, IndividualEntrepreneursSerializer, DiscountCardsSerializer, DealsSerializer

class TenantsViewSet (viewsets.ModelViewSet):
    queryset = Tenants.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TenantsrSerializer

class IndividualsViewSet (viewsets.ModelViewSet):
    queryset = Individuals.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IndividualsSerializer

class EntitsViewSet (viewsets.ModelViewSet):
    queryset = Entits.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EntitsSerializer

class IndividualEntrepreneursViewSet (viewsets.ModelViewSet):
    queryset = Individual_entrepreneurs.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IndividualEntrepreneursSerializer

class DiscountCardsViewSet (viewsets.ModelViewSet):
    queryset = Discount_cards.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DiscountCardsSerializer

class DealsViewSet (viewsets.ModelViewSet):
    queryset = Deals.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DealsSerializer

