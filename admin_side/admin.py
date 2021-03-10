from django.contrib import admin
# from .models import Tenants

# Register your models here.

# class TenantsAdmin (admin.ModelAdmin):
#     list_display = ('id', 'tenant_type', 'phone', 'email')
#     list_display_links = ('id', 'tenant_type')
#     search_fields = ('id', 'tenant_type', 'phone', 'email')
#     list_filter = ('tenant_type')

# admin.site.register(Tenants, TenantsAdmin)

from .models import Tenants, Individuals, Entits, Individual_entrepreneurs, Discount_cards, Deals

# from import_export.admin import ImportExportActionModelAdmin

class TenantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant_type', 'phone', 'email')
    list_filter = ('id', 'tenant_type')
    search_fields = ('id', 'tenant_type', 'phone', 'email')

class IndividualsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'surname', 'name', 'patronymic', 'passport_series', 'passport_number')
    list_filter = ('id', 'tenant')
    search_fields = ('id', 'tenant', 'surname')

class EntitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'company_name', 'inn', 'ogrn', 'address')
    list_filter = ('id', 'tenant')
    search_fields = ('id', 'tenant', 'company_name')

# class CarAdmin(ImportExportActionModelAdmin):
#     list_display = ('id', 'brand', 'model_name', 'model_details', 'number', 'color')
#     list_filter = ('brand', 'model_name', 'color')
#     search_fields = ('id', 'model_details', 'number')

# class StreetAdmin(ImportExportActionModelAdmin):
#     list_display = ('id', 'street', 'area')
#     list_filter = ('area',)
#     search_fields = ('id', 'street')

# class AvailableCarAdmin(ImportExportActionModelAdmin):
#     list_display = ('id', 'car_id', 'driver', 'street')
#     list_filter = ('street',)
#     search_fields = ('id', 'car_id', 'driver')

admin.site.register(Tenants, TenantsAdmin)
# admin.site.register(ModelDetail, ModelDetailAdmin)
# admin.site.register(Car, CarAdmin)
# admin.site.register(Street, StreetAdmin)
# admin.site.register(AvailableCar, AvailableCarAdmin)


