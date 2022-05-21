from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', ctx)


def detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {
        'post': post
    }
    return render(request, 'blog/detail.html', ctx)