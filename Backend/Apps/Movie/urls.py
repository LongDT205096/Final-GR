from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.MovieView.as_view(), name='movie'),
    path('detail/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('detail/<int:pk>/review/', views.UserReviewView.as_view(), name='review'),
    path('detail/<int:pk>/review/<int:review_pk>/update/', views.UpdateReviewView.as_view(), name='update_review'),
    path('detail/<int:pk>/review/<int:review_pk>/delete/', views.DeleteReviewView.as_view(), name='delete_review'),
]
