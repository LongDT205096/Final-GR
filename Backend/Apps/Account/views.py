from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pyrebase

from .serializer import AccountSerializer

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
            serializer.save()
			
            try:
                user = authe.create_user_with_email_and_password(serializer.data['email'], serializer.data['password'])
                
            except:
                return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
			
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        try:
            user = authe.sign_in_with_email_and_password(serializer.data['email'], serializer.data['password'])
            request.session['uid'] = str(user['idToken'])
            return Response(user, status=status.HTTP_200_OK)
        
        except:
            message = {"message": "Invalid credentials"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        authe.logout(request.session['uid'])
        del request.session['uid']
        return Response(status=status.HTTP_200_OK)
    


