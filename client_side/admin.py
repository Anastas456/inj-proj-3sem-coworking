from django.contrib import admin
from .models import Premises, Premises_types, Rates, Additional_services
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

admin.site.register(Premises, PremisesAdmin)
admin.site.register(Premises_types, PremisesTypesAdmin)
admin.site.register(Rates, RatesAdmin)
admin.site.register(Additional_services, AdditionalServicesAdmin)