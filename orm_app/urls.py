from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import employees_list, home, apply, customers_list, customer_form

urlpatterns = [
    path('', home, name='home'),
    path('employees/', employees_list, name='employees'),
    path('apply/', apply, name='apply'),
    path('list/', customers_list, name='customers_list'),
    path('customers/', customers_list, name='customers-list'),
    path('customer-form/', customer_form, name='customer-form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)