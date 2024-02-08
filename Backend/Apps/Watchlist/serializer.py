from rest_framework import serializers

from ..Movie.models import Movie
from .models import Watchlist, MovieInWatchlist

class WatchlistSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    class Meta:
        model = Watchlist
        fields = ('id', 'name', 'description', 'isPublic', 'user', 'movies')

    def get_movies(self, obj):
        try:
            objects = MovieInWatchlist.objects.filter(watchlist=obj.id)
            return [object.movie.title for object in objects]
        except:
            return []


class MovieInWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'
