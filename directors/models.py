from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    born = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    biography = models.TextField(max_length=20000)
    movies = models.ManyToManyField('movies.Movies', related_name='director_movies')

    def __str__(self):
        return self.name
