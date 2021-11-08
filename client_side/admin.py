# from re import search
from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Premises, Premises_types, Rates, Additional_services, Rent_form
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class PremisesAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'premise_type', 'square', 'number_of_workplaces', 'address')
    list_filter = ('id', 'premise_type', 'square', 'number_of_workplaces')
    search_fields = ('id', 'premise_type', 'square', 'number_of_workplaces', 'address')

class PremisesTypesAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'type')
    list_filter = ('id','type')
    search_fields = ('id','type') 

class RatesAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'premise_type', 'rental_time', 'fixed_or_non_fixed', 'price')
    list_filter = ('id', 'premise_type', 'rental_time', 'fixed_or_non_fixed')
    search_fields = ('id', 'premise_type', 'rental_time', 'fixed_or_non_fixed', 'price')

class AdditionalServicesAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_filter = ('id', 'name', 'price')
    search_fields = ('id', 'name', 'price')

class RentFormAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'client_name', 'email', 'phone', 'description')
    list_filter = ('id', 'client_name', 'email', 'phone')
    search_fields = ('id', 'client_name', 'email', 'phone', 'description')

admin.site.register(Premises, PremisesAdmin)
admin.site.register(Premises_types, PremisesTypesAdmin)
admin.site.register(Rates, RatesAdmin)
admin.site.register(Additional_services, AdditionalServicesAdmin)
admin.site.register(Rent_form, RentFormAdmin)