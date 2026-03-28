from django.shortcuts import render
from .models import Jobs, Employees
from .forms import ApplicationForm


def employees_list(request):
    employees = Employees.objects.select_related('department', 'job').all()
    return render(request, 'employees_list.html', {'employees': employees})


def home(request):
    return render(request, 'home.html')


def apply(request):
    success = False

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()          # saves to database
            success = True
            form = ApplicationForm()  # reset form after success
    else:
        form = ApplicationForm()  # empty form for GET request

    return render(request, 'apply.html', {'form': form, 'success': success})