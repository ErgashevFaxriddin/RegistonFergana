from django.shortcuts import render
from orm_app.models import Jobs


def home_view(request):
    all_jobs = Jobs.objects.all()

    context = {
        'jobs':all_jobs
    }

    return render(request, 'index.html', context)