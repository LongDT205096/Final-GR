from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    born = models.CharField(max_length=100)
    biography = models.TextField(max_length=10000, blank=True, null=True)
    movies = models.ManyToManyField('Movie.Movie', related_name="actor_movies", blank=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class actorVideo(models.Model):
    url = models.CharField(max_length=200)
    actor = models.ForeignKey(Actor, related_name='actors_video', on_delete=models.CASCADE)
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title
