from django.urls import path
from django.contrib import admin
from config.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.home_view(), name='first_view'),
]