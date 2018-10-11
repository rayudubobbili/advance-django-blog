from blog.models import Post
from django.shortcuts import render, redirect
from . import models


def facebook(request, slug):
    blog_post = Post.objects.get(slug=slug)
    if blog_post in [post.post for post in models.Facebook.objects.all()]:
        fb = models.Facebook.objects.get(post=blog_post)
        fb.share += 1
        fb.post = blog_post
        fb.save()
        return redirect('blog:detailview', slug=slug)
    else:
        models.Facebook.objects.create(share=1, post=blog_post)
        return redirect('blog:detailview', slug=slug)
    return render(request, 'blog/detailview.html', {'post': blog_post})


def google_plus(request, slug):
    blog_post = Post.objects.get(slug=slug)
    if blog_post in [post.post for post in models.Google_plus.objects.all()]:
        gplus = models.Google_plus.objects.get(post=blog_post)
        gplus.share += 1
        gplus.post = blog_post
        gplus.save()
        return redirect('blog:detailview', slug=slug)
    else:
        models.Google_plus.objects.create(share=1, post=blog_post)
        return redirect('blog:detailview', slug=slug)
    return render(request, 'blog/detailview.html', {'post': blog_post})


def twitter(request, slug):
    blog_post = Post.objects.get(slug=slug)
    if blog_post in [post.post for post in models.Twitter.objects.all()]:
        twitter = models.Twitter.objects.get(post=blog_post)
        twitter.share += 1
        twitter.post = blog_post
        twitter.save()
        return redirect('blog:detailview', slug=slug)
    else:
        models.Twitter.objects.create(share=1, post=blog_post)
        return redirect('blog:detailview', slug=slug)
    return render(request, 'blog/detailview.html', {'post': blog_post})


def reddit(request, slug):
    blog_post = Post.objects.get(slug=slug)
    if blog_post in [post.post for post in models.Reddit.objects.all()]:
        reddit = models.Reddit.objects.get(post=blog_post)
        reddit.share += 1
        reddit.post = blog_post
        reddit.save()
        return redirect('blog:detailview', slug=slug)
    else:
        models.Reddit.objects.create(share=1, post=blog_post)
        return redirect('blog:detailview', slug=slug)
    return render(request, 'blog/detailview.html', {'post': blog_post})


