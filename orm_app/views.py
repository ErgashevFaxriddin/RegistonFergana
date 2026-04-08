from django.shortcuts import render, redirect
from .models import Employees
from .forms import ApplicationForm


def home(request):
    return render(request, 'home.html')


def employees_list(request):
    employees = Employees.objects.select_related('department', 'job').all()
    return render(request, 'employees_list.html', {
        'employees': employees
    })


def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {
        'form': form
    })