from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class Post_list_view(ListView):
    model = Post
    template_name = 'blog/listview.html'


class Post_detail_view(DetailView):
    model = Post
    template_name = 'blog/detialview.html'
