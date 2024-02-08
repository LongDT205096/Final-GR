from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from .models import Watchlist, MovieInWatchlist
from .serializer import WatchlistSerializer

class WatchlistsView(APIView):
    def get(self, request):
        watchlists = Watchlist.objects.filter(user=request.user.id)
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['user'] = request.user.id
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class WatchlistDetailView(APIView):
    def get(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(id=pk)
        except:
            return Response({"error": "Watchlist not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(watchlist)
        serializer.data['movies'] = serializer.get_movies(watchlist)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        watchlist = Watchlist.objects.get(id=pk)        
        serializer = WatchlistSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Watchlist updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            watchlist = Watchlist.objects.get(id=request.data['id'])
        except:
            return Response({"error": "Watchlist not found"}, status=status.HTTP_404_NOT_FOUND)
        
        watchlist.delete()
        return Response({"success": "Watchlist deleted"}, status=status.HTTP_200_OK)
    

class ModifyMovieToWatchlist(APIView):   
    def post(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(id=pk)
        except:
            return Response({"error": "Watchlist not found"}, status=status.HTTP_404_NOT_FOUND)
        
        add = MovieInWatchlist(watchlist=watchlist, movie_id=request.data['movie_id'])
        add.save()
        return Response({"success": "Movie added to watchlist"}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(id=pk)
        except:
            return Response({"error": "Watchlist not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            movie = MovieInWatchlist.objects.get(watchlist=watchlist, movie_id=request.data['movie_id'])
        except:
            return Response({"error": "Movie not found in watchlist"}, status=status.HTTP_404_NOT_FOUND)
        
        movie.delete()
        return Response({"success": "Movie removed from watchlist"}, status=status.HTTP_200_OK)
