from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
import pyrebase

from .serializer import AccountSerializer
from .models import Account
from ..User.models import User

config = {
	'apiKey': "AIzaSyBo8aZIf-kUIUZvWdv2BRg4_tJ9SRj5jnA",
    'authDomain': "final-gr.firebaseapp.com",
    'projectId': "final-gr",
    'databaseURL': "https://final-gr-default-rtdb.firebaseio.com/",
    'storageBucket': "final-gr.appspot.com",
    'messagingSenderId': "456995198263",
    'appId': "1:456995198263:web:1ff3cf770e98e332fa36b2",
    'measurementId': "G-JV43SF5BD5"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


class RegisterView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
		
        if serializer.is_valid():
            try:
                user = authe.create_user_with_email_and_password(serializer.validated_data['email'], serializer.validated_data['password'])
                link = authe.send_email_verification(user['idToken'])
            except:
                return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = authe.sign_in_with_email_and_password(serializer.data['email'], serializer.data['password'])
                
                if not authe.get_account_info(user['idToken'])['users'][0]['emailVerified']:
                    return Response({"error": "Email not verified"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

            request.session['uid'] = str(user['idToken'])
            return Response(user, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        try:
            del request.session['uid']

        except:
            return Response({"message": "User not logged in"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "Logout succeeded"}, status=status.HTTP_200_OK)
    

class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            authe.send_password_reset_email(request.data['email'])
        except:
            return Response({"error": "Invalid email"}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"message": "Reset password email sent"}, status=status.HTTP_200_OK)
