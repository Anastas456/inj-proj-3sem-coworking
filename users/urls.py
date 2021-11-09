from django.conf.urls import url
from .views import  CreateUserAPIView, authenticate_user

app_name = 'users'
urlpatterns = [
    url(r'^register-user$', CreateUserAPIView.as_view()),
    url(r'^login-user/$', authenticate_user),
]