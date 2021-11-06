from django.urls.conf import include, path
from django.conf.urls import url
from rest_framework import routers

from .api import TenantsViewSet, IndividualsViewSet, EntitsViewSet, IndividualEntrepreneursViewSet, DiscountCardsViewSet, DealsViewSet
from client_side.api import PremisesViewSet, PremisesTypesViewSet, RatesViewSet, AdditionalServicesViewSet
from admin_side.views import CustomAuthToken, ProfileView, premise_bytype_list, tenant_list, tenant_detail


router = routers.DefaultRouter()
router.register('api/tenants', TenantsViewSet, 'tenants')
router.register('api/individuals', IndividualsViewSet, 'individuals')
router.register('api/entits', EntitsViewSet, 'entits')
router.register('api/individualentrepreneurs', IndividualEntrepreneursViewSet, 'individualentrepreneurs')
router.register('api/discountcards', DiscountCardsViewSet, 'discountcards')
router.register('api/deals', DealsViewSet, 'deals')

router.register('api/premises', PremisesViewSet, 'premises')
router.register('api/premisestypes', PremisesTypesViewSet, 'premisestypes')
router.register('api/rates', RatesViewSet, 'rates')
router.register('api/additionalservices', AdditionalServicesViewSet, 'additionalservices')

# router.register(r'api/users', UserViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api/auth/', CustomAuthToken.as_view()),
    path('api/profile/', ProfileView.as_view())
]
urlpatterns+=[
    url(r'^api/tenants$', tenant_list),
    url(r'^api/tenants/(?P<pk>[0-9]+)$', tenant_detail),
    url(r'^api/premises$', premise_bytype_list),
]