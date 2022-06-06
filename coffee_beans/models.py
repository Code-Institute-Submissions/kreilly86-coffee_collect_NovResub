from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft")), ((1, "Published"))


class Post(models.Model):
    producer = models.CharField(max_length=50, unique=False)
    region = models.CharField(max_length=50, unique=False)
    variety = models.CharField(max_length=50, unique=False)
    process = models.CharField(max_length=50, unique=False)
    flavournotes = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=50, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='coffee_likes', blank=True)


class Meta:
    ordering = ['-region']


def __str__(self):
    return self.title


def number_of_likes(self):
    return self.likes.count()
