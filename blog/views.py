from django.shortcuts import render, redirect
from .models import Post, Category, Tags, Comments
from .forms import ContactForm, CommentsForm


def homepage(request):
    posts = Post.objects.filter(publish=True)[:6]
    form = ContactForm()
    # FIXME: contact form on footer is not working besides homepage, fix it or remove it
    context = {'posts':posts, 'form':form}
    return render(request, 'blog/homepage.html', context)

def post_listview(request):
    posts = Post.objects.filter(publish=True)
    context = {'posts':posts}
    return render(request, 'blog/listview.html', context)

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
    context = {'post':post, 'form':form, 'comments':comments}
    return render(request, 'blog/detailview.html', context)

def category_listview(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'blog/category-listview.html', context)

def category_detailView(request, category):
    category = Post.objects.filter(category=category)
    context = {'category':category}
    return render(request,'blog/category-detailview.html', context)

def tag_listview(request):
    tags = Tags.objects.all()
    context = {'tags':tags}
    return render(request, 'blog/tag-listview.html', context)

def tag_detailview(request, tag):
    posts = Post.objects.filter(tags__tag = tag)
    context = {'posts':posts}
    return render(request, 'blog/tag-detailview.html', context)

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
            # TODO: Send email to admin with form details
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'blog/contact.html', context)

# Like function need to be completed
