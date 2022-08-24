from django.shortcuts import render, get_object_or_404
from .models import Post, Group


POSTS_COUNT = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.filter(group=True)[:POSTS_COUNT]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group)[:POSTS_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
