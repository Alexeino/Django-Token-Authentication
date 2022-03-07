from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',RegisterAPI.as_view(),name="register"),
    
    # Login Logout
    path('login/',obtain_auth_token,name="login")

]
