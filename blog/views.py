from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post, Category, Tags
from .forms import ContactForm, CommentsForm


def homepage(request):
    posts = Post.objects.filter(publish=True)[:6]
    form = ContactForm()
    # FIXME: contact form on footer is not working besides homepage, fix it or remove it
    return render(request, 'blog/homepage.html', {'posts':posts, 'form':form})

def post_listview(request):
    posts = Post.objects.filter(publish=True)
    return render(request, 'blog/listview.html', {'posts':posts})

class Post_detailview(DetailView):
    model = Post
    form = ContactForm()
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

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.name, form.email, form.subject, form.message)
            form = Contact.save()
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form':form})



# Create contactform and comments form
# comments can be commented by user and need approvel to display on post
# Like function need to be completed
