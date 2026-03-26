from django.shortcuts import render
from .models import Jobs, Employees


def employees_list(request):
    employees = Employees.objects.select_related('department', 'job').all()
    return render(request, 'employees_list.html', {'employees': employees})


def home(request):
    return render(request, 'home.html')