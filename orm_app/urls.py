from django.urls import path
from .views import employees_list, home

urlpatterns = [
    path('', home, name='home'),
    path('employees/', employees_list, name='employees_list'),
]