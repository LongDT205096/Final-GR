from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    born = models.CharField(max_length=100)
    biography = models.TextField(max_length=20000)
    image_url = models.CharField(max_length=200)
    movies = models.ManyToManyField('Movie.Movie', related_name="director_movies", blank=True)

    def __str__(self):
        return self.name
    

class directorVideo(models.Model):
    url = models.CharField(max_length=200)
    director = models.ForeignKey(Director, related_name='director_video', on_delete=models.CASCADE)
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title
