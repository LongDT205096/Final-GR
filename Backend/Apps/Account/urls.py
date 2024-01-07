from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('reset-password/', views.ResetPasswordView.as_view(), name="reset-password"),
    path('change-password/', views.ChangePasswordView.as_view(), name="change-password"),
]
