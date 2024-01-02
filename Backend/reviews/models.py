from django.db import models

# Create your models here.
class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movies', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.comment
