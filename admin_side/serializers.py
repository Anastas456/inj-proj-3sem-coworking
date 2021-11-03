# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tenants, Individuals, Entits, Individual_entrepreneurs, Discount_cards, Deals

class TenantsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenants
        fields = '__all__'

class IndividualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individuals
        fields = '__all__'

class EntitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entits
        fields = '__all__'

class IndividualEntrepreneursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual_entrepreneurs
        fields = '__all__'

class DiscountCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount_cards
        fields = '__all__'

class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
     
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name')
