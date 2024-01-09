from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=5000)
    stars_rate = models.FloatField(default=0.0)
    movie = models.ForeignKey('Movie.Movie', related_name='movie_review', on_delete=models.CASCADE)
    user = models.ForeignKey('User.User', related_name='user_review', on_delete=models.CASCADE)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
