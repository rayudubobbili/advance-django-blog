import markdown

from django.db import models
from django.urls import reverse


class Tags(models.Model):
    tag = models.SlugField(max_length=100)

    def __str__(self):
        return self.tag

    def get_absoulute_url(self):
        return reverse('blog:tag-detailview', kwargs={'slug':self.tag})

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Comments(models.Model):
    comment = models.TextField(default="null")

    #TODO: Create a function 'is_approved' to show comments if admin wants to unless delete comment

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Views(models.Model):
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.view

    class Meta:
        verbose_name = "View"
        verbose_name_plural = "Views"


class Likes(models.Model):
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.like

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"


class Category(models.Model):
    category = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.category

    def get_absoulute_url(self):
        return reverse('blog:category-detailview', kwargs={'slug':self.category})


class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete='CASCADE')
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=600)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey('Category', default="", to_field="category", on_delete='CASCADE')
    tags = models.ManyToManyField('Tags')
    body = models.TextField()
    body_html = models.TextField(editable=False)
    publish = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    feature_image = models.ImageField(upload_to="static/img/")
    comments = models.ManyToManyField('Comments', blank=True)
    views = models.ManyToManyField('Views', blank=True)
    likes = models.ManyToManyField('likes', blank=True)


    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ['-published']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.body_html = markdown.markdown(self.body)
        super().save(*args, **kwargs)

    def get_absoulute_url(self):
        return reverse('blog:detailview', kwargs={'slug':self.slug})

