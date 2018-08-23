from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def homepage(request):
    posts = Post.objects.all()[:6]
    return render(request, 'blog/homepage.html', {'posts':posts})


class Post_list_view(ListView):
    model = Post
    template_name = 'blog/listview.html'


class Post_detail_view(DetailView):
    model = Post
    template_name = 'blog/detailview.html'
