from django.shortcuts import render
from .models import *


def home(request):
    # data = Data.objects.filter(dt__lte='2018-01-01')
    # print(data)
    posts = [Data.objects.latest('id')]
    cont = {'posts': posts}
    return render(request, 'home.html',cont)


def select_location(request):
    posts = [Data.objects.latest('id')]
    cont = {'posts': posts}
    return render(request, 'select_location.html', cont)


def campus_report(request):
    return render(request, 'campus_report.html')


def feedback(request):
    return render(request, 'feedback.html')