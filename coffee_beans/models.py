from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Coffee(models.Model):
    producer = models.CharField(max_length=50, unique=False)
    region = models.CharField(max_length=50, unique=False)
    variety = models.CharField(max_length=50, unique=False)
    process = models.CharField(max_length=50, unique=False)
    flavournotes = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=50, unique=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    approved = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
        related_name='user')

    class Meta:
        ordering = ['region']

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        self.slug = slugify(self.producer)
        super(Coffee, self).save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()
