from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .models import Movie, Genre, Review
from .serializer import MovieSerializer, ReviewSerializer
from ..Account.models import Account
from ..Actor.models import Actor
from ..Director.models import Director


class MovieView(APIView):
    def get(self, request):
        movie_list = MovieSerializer(Movie.objects.all(), many=True)
        for movie in movie_list.data:
            for genre_index in movie['genres']:
                genre = Genre.objects.get(pk=genre_index)
                movie['genres'][movie['genres'].index(genre.pk)] = genre.__str__()

            for actor_index in movie['actors']:
                actor = Actor.objects.get(pk=actor_index)
                movie['actors'][movie['actors'].index(actor.pk)] = actor.__str__()

            for director_index in movie['directors']:
                director = Director.objects.get(pk=director_index)
                movie['directors'][movie['directors'].index(director.pk)] = director.__str__()
        return Response(movie_list.data)


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
        your_reviews = ReviewSerializer(Review.objects.filter(movie=movie, user=request.user.id), many=True)
        all_reviews = Review.objects.all().filter(movie=movie).exclude(user=request.user.id)
        user_reviews = [ReviewSerializer(review).data for review in all_reviews if review.comment]
        
        return Response({'movie': movie_detail.data, 
                         'your_reviews': your_reviews.data,
                         'user_reviews': user_reviews,
                        })
    
    def post(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        request.data['movie'] = movie.pk
        request.data['user'] = request.user.id        
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            movie.ave_rating = movie.average_rating()
            movie.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateReviewView(APIView):
    def get(self, request, pk, review_pk):
        movie = Movie.objects.get(pk=pk)
        movie_detail = MovieSerializer(movie)
        your_review = ReviewSerializer(Review.objects.get(pk=review_pk))
        return Response({'movie': movie_detail.data, 
                         'your_review': your_review.data,
                        })

    def put(self, request, pk, review_pk):
        movie = Movie.objects.get(pk=pk)
        your_review = Review.objects.get(pk=review_pk)
        request.data['movie'] = movie.pk
        request.data['user'] = request.user.id
        new_review = ReviewSerializer(data=request.data)

        if new_review.is_valid():
            your_review.title = new_review.data['title']
            your_review.comment = new_review.data['comment']
            your_review.stars_rate = new_review.data['stars_rate']
            your_review.save()
            movie.ave_rating = movie.average_rating()
            movie.save()
            return Response(new_review.data)

        return Response(new_review.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteReviewView(APIView):
    def post(self, request, pk, review_pk):
        movie = Movie.objects.get(pk=pk)
        review = Review.objects.get(pk=review_pk)
        try:
            review.delete()
            movie.ave_rating = movie.average_rating()
            movie.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
