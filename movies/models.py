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
        ('Commercial', 'Commercial'),
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

class Movies(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    average_rating = models.FloatField(default=0.0)
    genre = models.ForeignKey(Genre, related_name='movie_genre', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    directors = models.ManyToManyField('directors.Director', related_name='movie_directors')
    actors = models.ManyToManyField('actors.Actor', related_name='movie_actors')
    duration = models.IntegerField()
    storyline = models.CharField(max_length=300)
    summary = models.CharField(max_length=500)
    synopsis = models.TextField(max_length=20000)
    
    def __str__(self) -> str:
        return self.title
    
class movieVideo(models.Model):
    url = models.CharField(max_length=200)
    movie = models.ForeignKey(Movies, related_name='movie_video', on_delete=models.CASCADE)
    is_trailer = models.BooleanField(default=False)
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.movie.title
