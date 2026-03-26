from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def index_page(request):
    pass