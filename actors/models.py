from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    born = models.CharField(max_length=100)
    actor = models.ForeignKey('movies.Movies', on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey('actors.actorVideo', on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.CharField(max_length=200)
    biography = models.TextField(max_length=20000)
    movies = models.ManyToManyField('movies.Movies', related_name='actor_movies')


    def __str__(self):
        return self.name

class actorVideo(models.Model):
    url = models.CharField(max_length=200)
    actors = models.ForeignKey(Actor, related_name='actors_video', on_delete=models.CASCADE)
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title
