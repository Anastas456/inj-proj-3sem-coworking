from django.conf.urls import url
from client_side.views import add_premise, form_rent_form, premise_bytype_list, premise_detail, rate_list 


app_name = 'client_side'
urlpatterns = [
    url(r'^premises$', premise_bytype_list),
    url(r'^add-premise$', add_premise),
    url(r'^premises/(?P<pk>[0-9]+)$', premise_detail),
    url(r'^rent-form$', form_rent_form),
    url(r'^rates$', rate_list)
]