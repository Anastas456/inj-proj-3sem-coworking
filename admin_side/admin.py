from django.contrib import admin
from .models import Tenants, Individuals, Entits, Individual_entrepreneurs, Discount_cards, Deals

def make_deals_in_progress(modeladmin, request, queryset):
    queryset.update(status='раб')
make_deals_in_progress.short_description = "Изменить статус сделок на 'в работе'"

def make_deals_done(modeladmin, request, queryset):
    queryset.update(status='вып')
make_deals_done.short_description = "Изменить статус сделок на 'выполнен'"


class TenantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant_name', 'tenant_type', 'phone', 'email')
    list_filter = ('id', 'tenant_name', 'tenant_type')
    search_fields = ('id', 'tenant_name', 'tenant_type', 'phone', 'email')

class IndividualsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'surname', 'name', 'patronymic', 'passport_series', 'passport_number')
    list_filter = ('id', 'tenant')
    search_fields = ('id', 'tenant', 'surname')

class EntitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'company_name', 'inn', 'ogrn', 'address')
    list_filter = ('id', 'tenant')
    search_fields = ('id', 'tenant', 'company_name')

class IndividualEntrepreneursAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'surname', 'name', 'patronymic', 'address', 'inn', 'ogrnip')
    list_filter = ('id', 'tenant')
    search_fields = ('id', 'tenant', 'surname')

class DiscountCardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'discount')
    list_filter = ('id', 'tenant', 'discount')
    search_fields = ('id', 'tenant', 'discount')

class DealsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'rate', 'premise', 'additional_services', 'start_of_lease', 'end_of_lease', 'date_of_signing_the_deal', 'discount', 'total_price', 'total_price', 'status')
    list_filter = ('id', 'tenant', 'total_price', 'status')
    search_fields = ('id', 'tenant', 'total_price', 'status')
    actions=[make_deals_in_progress, make_deals_done]


admin.site.register(Tenants, TenantsAdmin)
admin.site.register(Individuals, IndividualsAdmin)
admin.site.register(Entits, EntitsAdmin)
admin.site.register(Individual_entrepreneurs, IndividualEntrepreneursAdmin)
admin.site.register(Discount_cards, DiscountCardsAdmin)
admin.site.register(Deals, DealsAdmin)


