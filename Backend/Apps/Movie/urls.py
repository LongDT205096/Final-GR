from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('detail/<int:pk>/review/', views.UserReviewView.as_view(), name='review'),
]
