from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import employees_list, home, apply

urlpatterns = [
    path('', home, name='home'),
    path('employees/', employees_list, name='employees'),  # 👈 changed here
    path('apply/', apply, name='apply'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)