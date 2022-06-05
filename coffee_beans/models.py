from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft")), ((1, "Published"))


class Post(models.Model):
    producer = models.CharField(max_length=50, unique=True)
    region = models.CharField(max_length=50, unique=True)
    varietyprocess = models.CharField(max_length=50, unique=True)
    flavournotes = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='coffee_likes',blank=True)
    approved = models.BooleanField(default=False)


class Meta:
    ordering = ['-region']


def __str__(self):
    return self.title


def number_of_likes(self):
    return self.likes.count()
