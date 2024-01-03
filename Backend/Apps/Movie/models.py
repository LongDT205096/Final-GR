from django.db import models

# Create your models here.
class Genre(models.Model):
    GENRE_CHOICES = [
        ('Action', 1),
        ('Adventure', 2),
        ('Animation', 3),
        ('Biography', 4),
        ('Comedy', 5),
        ('Crime', 6),
        ('Commercial', 7),
        ('Documentary', 8),
        ('Drama', 9),
        ('Family', 10),
        ('Fantasy', 11),
        ('Film-Noir', 12),
        ('History', 13),
        ('Horror', 14),
        ('Musical', 15),
        ('Mystery', 16),
        ('Romance', 17),
        ('Sci-Fi', 18),
        ('Sport', 19),
        ('Thriller', 20),
        ('War', 21),
        ('Western', 22),
    ]
    name = models.CharField(max_length=20, choices=GENRE_CHOICES)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    average_rating = models.FloatField(default=0.0)
    genre = models.ForeignKey(Genre, related_name='movie_genre', on_delete=models.CASCADE)
    directors = models.ManyToManyField('Director.Director', related_name='movie_directors')
    actors = models.ManyToManyField('Actor.Actor', related_name='movie_actors')
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    duration = models.IntegerField()
    storyline = models.CharField(max_length=300)
    summary = models.CharField(max_length=500)
    synopsis = models.TextField(max_length=20000)
    
    def __str__(self) -> str:
        return self.title
    
class movieVideo(models.Model):
    url = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, related_name='movie_video', on_delete=models.CASCADE)
    is_trailer = models.BooleanField(default=False)
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.movie.title
