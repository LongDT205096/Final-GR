from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

# Create your views here.
from .serializer import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    UserUpdateSerializer
)

from .models import (
    User, 
    Account
)

class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = User.objects.get(account=pk)
        return Response({
                    "success": True,
                    "msg": "User profile retrieved successfully.",
                    "user": {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "phone": user.phone,
                        "bio": user.bio,
                        "birth_date": user.birth_date,
                        "country": user.country,
                    },
                },
            status=status.HTTP_200_OK,
        )


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                        "success": True, 
                        "user ID": user.id,
                        "msg": "Account created successfully."
                    },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    

class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"success": True, "msg": "Logout successfully."})
    

class UserProfileView(APIView):
    def get(self, request, pk):
        user = User.objects.get(account=pk)
        return Response({
                    "success": True,
                    "msg": "User profile retrieved successfully.",
                    "user": {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "phone": user.phone,
                        "bio": user.bio,
                        "birth_date": user.birth_date,
                        "country": user.country,
                    },
                },
            status=status.HTTP_200_OK,
        )
