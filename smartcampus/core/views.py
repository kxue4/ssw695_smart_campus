from django.shortcuts import render
from .models import Data


def home(request):
        posts = Data.objects.all()
        args = { 'posts': posts }
        return render(request ,'home.html', args)

