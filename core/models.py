from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username


class Tweet(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    tip = models.TextField()
    author = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.tip
    
    class Meta:
        ordering = '-timestamp',


class Link(models.Model):
    url = models.URLField()
    tweet = models.ForeignKey(Tweet, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.url
