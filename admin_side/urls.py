from rest_framework import routers
from .api import TenantsViewSet, IndividualsViewSet, EntitsViewSet, IndividualEntrepreneursViewSet, DiscountCardsViewSet, DealsViewSet
from client_side.api import PremisesViewSet, PremisesTypesViewSet, RatesViewSet, AdditionalServicesViewSet

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



urlpatterns = router.urls