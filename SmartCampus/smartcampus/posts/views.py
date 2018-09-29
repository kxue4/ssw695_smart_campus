from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request , 'posts/index.html', context)
# Create your views here.
