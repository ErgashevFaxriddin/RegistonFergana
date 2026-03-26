from django.urls import path
from .views import home_view, job_detail_view, jobs_list

urlpatterns = [
    path('', home_view, name='home_view'),
    path('jobs/', jobs_list, name='jobs_list'),
    path('jobs/<int:pk>/', job_detail_view, name='job_detail'),
]