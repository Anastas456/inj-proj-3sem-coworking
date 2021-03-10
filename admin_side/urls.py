from rest_framework import routers
from .api import TenantsViewSet, IndividualsViewSet, EntitsViewSet, IndividualEntrepreneursViewSet, DiscountCardsViewSet, DealsViewSet

router = routers.DefaultRouter()
router.register('api/tenants', TenantsViewSet, 'tenants')
router.register('api/individuals', IndividualsViewSet, 'individuals')
router.register('api/entits', EntitsViewSet, 'entits')
router.register('api/individualentrepreneurs', IndividualEntrepreneursViewSet, 'individualentrepreneurs')
router.register('api/discountcards', DiscountCardsViewSet, 'discountcards')
router.register('api/deals', DealsViewSet, 'deals')
urlpatterns = router.urls