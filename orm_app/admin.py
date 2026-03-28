from django.contrib import admin
from orm_app.models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'job']
    list_filter = ['job']
    search_fields = ['name', 'email', 'phone']
    ordering = ['-id']