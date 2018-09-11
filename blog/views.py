from django.shortcuts import render, redirect
from .models import Post, Category, Tags, Comments
from .forms import ContactForm, CommentsForm


def homepage(request):
    posts = Post.objects.filter(publish=True)[:6]
    form = ContactForm()
    # FIXME: contact form on footer is not working besides homepage, fix it or remove it
    return render(request, 'blog/homepage.html', {'posts':posts, 'form':form})

def post_listview(request):
    posts = Post.objects.filter(publish=True)
    return render(request, 'blog/listview.html', {'posts':posts})


def post_detailview(request, slug):
    comments = Comments.objects.filter(post=slug)
    post_filter = Post.objects.filter(slug=slug)
    for post in post_filter:
        post
    if request.method != "POST":
        form = CommentsForm()
    else:
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            form.save_m2m() # Save many to many relations
            return redirect('blog:detailview', slug=slug)
    return render(request, 'blog/detailview.html', {'post':post, 'form':form, 'comments':comments})


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
            pass
            # TODO: Send email to admin with form details
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form':form})

# Like function need to be completed
