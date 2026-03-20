from .views import *
from django.urls import path
urlpatterns = [
    path('add/',add_laptop, name='add_laptop'),
    path('laptop/', laptop_list, name='laptop_list'),
]