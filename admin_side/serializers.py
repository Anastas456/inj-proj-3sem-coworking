from django.contrib.auth.models import User
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user