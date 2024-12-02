from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.db import models

from django.db import models
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=250)
    director = models.CharField(max_length=300)
    cast = models.CharField(max_length=300)
    release_date = models.DateField()
    description = models.TextField()
    rating = models.FloatField(default=0)  # Set rating constraints
    image = models.ImageField(upload_to='pics')  # Set default image
    youtube_url = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, null=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username