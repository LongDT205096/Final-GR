from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import User
from .serializer import (
    ProfileSerializer,
    ProfileUpdateSerializer
)


class ProfileView(APIView):
    def get(self, request):
        try:
            profile = User.objects.get(account_id=request.user.id)
        except:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileUpdateView(APIView):
    def get(self, request):
        try:
            profile = User.objects.get(account_id=request.user.id)
        except:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request):
        try:
            profile = User.objects.get(account_id=request.user.id)
        except:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileUpdateSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Profile updated"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
