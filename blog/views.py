from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post, Category, Tags


def homepage(request):
    posts = Post.objects.filter(publish=True)[:6]
    return render(request, 'blog/homepage.html', {'posts':posts})

def post_listview(request):
    posts = Post.objects.filter(publish=True)
    return render(request, 'blog/listview.html', {'posts':posts})

class Post_detailview(DetailView):
    model = Post
    template_name = "blog/detailview.html"

def category_listview(request):
    categories = Category.objects.all()
    return render(request, 'blog/category-listview.html', {'categories': categories})

def category_detailView(request, category):
    category = Post.objects.filter(category=category)
    return render(request,'blog/category-detailview.html', {'category': category})

def tag_listview(request):
    tags = Tags.objects.all()
    return render(request, 'blog/tag-listview.html', {'tags':tags})

def tag_detailview(request, tag):
    posts = Post.objects.filter(tags__tag = tag)
    return render(request, 'blog/tag-detailview.html', {'posts':posts})
