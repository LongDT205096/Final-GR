from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.ActorDetailView.as_view(), name='actor_detail'),
]
