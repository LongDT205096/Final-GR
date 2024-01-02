from django.contrib import admin
from .models import Movies, Genre, movieVideo

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'year',
        'average_rating',
        'genre',
        'description',
        'image_url',
        'duration',
        'storyline',
        'summary',
        'synopsis'
    )

    list_filter = ('year', 'genre')
    search_fields = ('title', 'year', 'genre')


admin.site.register(Movies)
admin.site.register(Genre)
admin.site.register(movieVideo)
