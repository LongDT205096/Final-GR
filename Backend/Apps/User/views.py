from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializer import (
    ProfileSerializer,
    ProfileUpdateSerializer
)

from .models import User


class NewProfileView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Profile created"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    def get(self, request):
        try:
            profile = User.objects.get(account__uid=request.session['uid'])
        except:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileUpdateView(APIView):
    def put(self, request):
        try:
            profile = User.objects.get(account__uid=request.session['uid'])
        except:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileUpdateSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Profile updated"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
