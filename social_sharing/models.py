from django.db import models
from django.urls import reverse


class Facebook(models.Model):
    share = models.IntegerField(default=0)
    post = models.ForeignKey('blog.post', to_field='slug', on_delete='CASCADE')


    def __str__(self):
        return str(self.post)


    def get_absoulute_url(self):
        return reverse('social_sharing:facebook_share', kwargs={'slug': self.post})


class Google_plus(models.Model):
    share = models.IntegerField(default=0)
    post = models.ForeignKey('blog.post', to_field='slug', on_delete='CASCADE')


    def __str__(self):
        return str(self.post)


    def get_absoulute_url(self):
        return reverse('social_sharing:Google_plus_share', kwargs={'slug': self.post})


class Twitter(models.Model):
    share = models.IntegerField(default=0)
    post = models.ForeignKey('blog.post', to_field='slug', on_delete='CASCADE')


    def __str__(self):
        return str(self.post)


    def get_absoulute_url(self):
        return reverse('social_sharing:twitter_share', kwargs={'slug': self.post})


class Reddit(models.Model):
    share = models.IntegerField(default=0)
    post = models.ForeignKey('blog.post', to_field='slug', on_delete='CASCADE')


    def __str__(self):
        return str(self.post)


    def get_absoulute_url(self):
        return reverse('social_sharing:reddit_share', kwargs={'slug': self.post})
