from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .models import Movie
from .serializer import MovieSerializer


class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
