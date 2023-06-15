from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    genres = models.ManyToManyField('Genre')
    rating = models.CharField(max_length=10)
    year = models.PositiveIntegerField()
    metacritic_rating = models.PositiveIntegerField()
    runtime = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name