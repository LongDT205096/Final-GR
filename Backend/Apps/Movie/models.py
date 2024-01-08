from django.db import models

# Create your models here.
class Genre(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Biography', 'Biography'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Film-Noir', 'Film-Noir'),
        ('History', 'History'),
        ('Horror', 'Horror'),
        ('Music', 'Music'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Sport', 'Sport'),
        ('Thriller', 'Thriller'),
        ('War', 'War'),
        ('Western', 'Western'),
    ]
    name = models.CharField(max_length=20, choices=GENRE_CHOICES)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    average_rating = models.FloatField(default=0.0)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    directors = models.ManyToManyField('Director.Director', related_name='movie_directors')
    actors = models.ManyToManyField('Actor.Actor', related_name='movie_actors')
    image_url = models.CharField(max_length=200, blank=True, null=True)
    duration = models.IntegerField()
    description = models.CharField(max_length=5000, blank=True, null=True)
    summary = models.CharField(max_length=2000, blank=True, null=True)
    storyline = models.TextField(max_length=15000, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
class movieVideo(models.Model):
    url = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, related_name='movie_video', on_delete=models.CASCADE)
    is_trailer = models.BooleanField(default=False)
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.movie.title
