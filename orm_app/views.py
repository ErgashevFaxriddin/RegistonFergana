from django.shortcuts import render, redirect
from .models import Employees, Customer
from .forms import ApplicationForm, CustomerForm


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

def customer_form(request):
    form = CustomerForm(request.POST)
    if request.POST and form.is_valid():
        return redirect("customers-list")
    ctx = {
        "form": form
    }
    return render(request, "form.html", ctx)

def customers_list(request):
    customers = Customer.objects.all()
    ctx = {
        'customers': customers
    }
    return render(request, 'table.html', ctx)