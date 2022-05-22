from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

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

def create(request):
    ctx = {}
    if request.method == 'GET':
        ctx['form'] = PostForm
        return render(request, 'blog/create.html', ctx)
    elif request.method == 'POST':
        Post.objects.create(title=request.POST.get('title', None),
                            content=request.POST.get('content', None),
                            create_at=timezone.now())
        return redirect(to='index')