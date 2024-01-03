from django.db import models

# Create your models here.
class Watchlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    isPublic = models.BooleanField(default=False)
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class MovieInWatchlist(models.Model):
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie.Movie', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.movie.title
