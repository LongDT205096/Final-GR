from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.WatchlistsView.as_view()),
    path('detail/<int:pk>/', views.WatchlistDetailView.as_view()),
    path('detail/<int:pk>/modify-movie', views.ModifyMovieToWatchlist.as_view()),
]
