from django.urls import path
from .views import employees_list, home, apply

urlpatterns = [
    path('', home, name='home'),
    path('employees/', employees_list, name='employees'),  # 👈 changed here
    path('apply/', apply, name='apply'),
]