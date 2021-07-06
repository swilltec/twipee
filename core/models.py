from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    
    def __str__(self):
        return self.username


class Link(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Tweet(models.Model):
    timestamp=models.DateTimeField(blank=True, null=True)
    tip=models.TextField()
    link=models.ForeignKey(Link, null=True, on_delete=models.SET_NULL)
    author=models.CharField(blank=True, null=True, max_length=100)