from django.urls import path

from .views import *

urlpatterns = [
    path('comp/add/',add_computer, name='add_computer'),
    path('', home_page, name='home_page'),
    path('comp/', comp_list, name='comp_list'),
    path('comp/info/<int:pk>/', computer_info, name='comp_info'),
    path('delete/<int:pk>/', delete_computer, name='delete_computer'),
]