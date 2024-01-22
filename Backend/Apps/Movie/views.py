from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .models import Movie, Genre, Review
from .serializer import MovieSerializer, ReviewSerializer
from ..Account.models import Account
from ..Actor.models import Actor
from ..Director.models import Director


class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        
        for genre_index in serializer.data['genres']:
            genre = Genre.objects.get(pk=genre_index)
            serializer.data['genres'][serializer.data['genres'].index(genre.pk)] = genre.__str__()

        for actor_index in serializer.data['actors']:
            actor = Actor.objects.get(pk=actor_index)
            serializer.data['actors'][serializer.data['actors'].index(actor.pk)] = actor.__str__()

        for director_index in serializer.data['directors']:
            director = Director.objects.get(pk=director_index)
            serializer.data['directors'][serializer.data['directors'].index(director.pk)] = director.__str__()

        return Response(serializer.data)


class UserReviewView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie_detail = MovieSerializer(movie)
        user_reviews = Review.objects.filter(movie=movie)
        user_reviews = [review for review in user_reviews if review.comment]
        user = Account.objects.get(pk=request.user.id)
        your_review = ReviewSerializer(Review.objects.filter(movie=movie, user=user.id), many=True)
        return Response({'movie': movie_detail.data, 
                         'your_review': your_review.data,
                         'user_reviews': [ReviewSerializer(review).data for review in user_reviews if review.user != user.id]
                        })
    
    def post(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        request.data['movie'] = movie.pk
        
        serializer = ReviewSerializer(data=request.data)

        print(request.data)
        if serializer.is_valid():
            movie.ave_rating = movie.average_rating()
            movie.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

