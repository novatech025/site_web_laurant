from django.urls import path
from .views import *





app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('realisation/',realisation,name='realisation'),
]
