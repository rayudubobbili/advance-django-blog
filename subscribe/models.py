from django.db import models


class Subscribers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
