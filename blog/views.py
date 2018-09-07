from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post


def homepage(request):
    posts = Post.objects.filter(publish=True)[:6]
    return render(request, 'blog/homepage.html', {'posts':posts})

def post_listview(request):
    posts = Post.objects.filter(publish=True)
    return render(request, 'blog/listview.html', {'posts':posts})

class Post_detailview(DetailView):
    model = Post
    template_name = "blog/detailview.html"
