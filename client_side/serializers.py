from django.db.models import fields
from rest_framework import serializers
from .models import Premises, Premises_types, Rates, Additional_services, Rent_form

class PremisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premises
        fields = '__all__'

class PremisesTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premises_types
        fields = '__all__'

class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = '__all__'

class AdditionalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional_services
        fields = '__all__'

class RentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent_form
        fields = '__all__'