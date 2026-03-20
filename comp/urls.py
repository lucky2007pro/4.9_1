from .views import *
from django.urls import path
urlpatterns = [
    path('comp/add/',add_computer, name='add_computer'),
    path('', home_page, name='home_page'),
    path('comp/', comp_list, name='comp_list'),
]