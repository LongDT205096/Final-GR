from django.urls import path
from . import views

urlpatterns = [
    path('actor/<int:pk>/', views.ActorDetailView.as_view()),
]
