from django.shortcuts import render
from .models import Data


def home(request):
    posts = Data.objects.all()
    args = {'posts': posts}
    return render(request, 'home.html', args)


def select_location(request):
    return render(request, 'select_location.html')


def campus_report(request):
    return render(request, 'campus_report.html')


def feedback(request):
    return render(request, 'feedback.html')