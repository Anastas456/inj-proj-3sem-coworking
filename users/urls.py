from django.conf.urls import url
# from rest_framework_jwt.views import obtain_jwt_token

from .views import LoginAPIView, RegistrationAPIView

app_name = 'users'
urlpatterns = [
    # path('users/', RegistrationAPIView.as_view()),
    url(r'^register-user$', RegistrationAPIView.as_view()),
    # url(r'^auth-user/', obtain_jwt_token),
    url(r'^login-user/$', LoginAPIView.as_view())
]