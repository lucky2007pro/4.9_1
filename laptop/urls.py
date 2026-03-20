from django.urls import path

from .views import *

urlpatterns = [
    path('add/',add_laptop, name='add_laptop'),
    path('laptop/', laptop_list, name='laptop_list'),
    path('laptop/info/<int:pk>/', laptop_info, name='laptop_info'),
    path('delete/<int:pk>/', delete_laptop, name='delete_laptop'),
]