from django.urls import path
from .views import home_view, job_detail_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('jobs/<int:pk>/', job_detail_view, name='job_detail')
]