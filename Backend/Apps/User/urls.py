from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/new/', views.NewProfileView.as_view(), name='profile-new'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
]
