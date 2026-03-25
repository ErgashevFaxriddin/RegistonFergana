from django.shortcuts import render, get_object_or_404
from orm_app.models import Jobs


def home_view(request):
    all_jobs = Jobs.objects.all()

    context = {
        'jobs':all_jobs
    }

    return render(request, 'index.html', context)


def job_detail_view(request, pk):
    job = get_object_or_404(Jobs, pk=pk)

    context = {
        'job': job
    }

    return render(request, 'job_detail.html', context)