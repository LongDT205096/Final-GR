from django.db import models

# Create your models here.
class Watchlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    isPublic = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class YourList(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey('movies.Movies', on_delete=models.CASCADE)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
