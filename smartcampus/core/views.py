from django.shortcuts import render
from .models import *


def home(request):
    # data = Data.objects.filter(dt__lte='2018-01-01')
    # print(data)
    return render(request, 'home.html')


def select_location(request):
    return render(request, 'select_location.html')


def campus_report(request):
    return render(request, 'campus_report.html')


def feedback(request):
    return render(request, 'feedback.html')