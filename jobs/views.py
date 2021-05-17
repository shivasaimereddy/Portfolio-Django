from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def home(request):
    jobs = Job.objects.all()
    print(jobs)
    return render(request, 'home.html', {'jobs': jobs})


def details(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'detail.html', {'job': job_detail})
