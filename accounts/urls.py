from django.urls import path
from .views import RegisterationView
urlpatterns = [
    path('',RegisterationView,name="registeration")
]
