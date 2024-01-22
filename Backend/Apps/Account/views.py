from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from firebase_admin import auth, initialize_app
import pyrebase

from .models import Account
from ..User.models import User
from .serializer import (
    AccountSerializer,
    ChangePasswordSerializer
)


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
default_app = initialize_app()

class RegisterView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
		
        if serializer.is_valid():
            try:
                user = authe.create_user_with_email_and_password(serializer.validated_data['email'], serializer.validated_data['password'])
                authe.send_email_verification(user['idToken'])
            except:
                return Response({"error": "Register failed"}, status=status.HTTP_400_BAD_REQUEST)
            
            new_accoount = serializer.save()
            new_user_profile = User(account=new_accoount)
            new_user_profile.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            email, password = serializer.validated_data.values()
            try:
                account = Account.objects.get(email=email)
            except account.DoesNotExist:
                return Response({"error": "Invalid account"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                if not account.check_password(password):
                    return Response({"error": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)
                
                fb_user = auth.get_user_by_email(email)
                if fb_user.email_verified == True:
                    if not account.is_active:
                        account.is_active = True
                        account.save()
                    login(request, account)

                    return Response({"id": account.id, "email": account.email}, status=status.HTTP_200_OK)
                print("email not verified")
                return Response({"error": "Account is not active"}, status=status.HTTP_400_BAD_REQUEST)
            
            except:
                return Response({"error": "Invalid credentials. Check your account again."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                logout(request)
                return Response({"Message": "Logout succeeded"}, status=status.HTTP_200_OK)
            except:
                return Response({"Message": "Logout failed"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"Message": "User hasn't login"}, status=status.HTTP_200_OK)
    

# cần xem xét lại cách sử dụng firebase và mysql
class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)

    # def post(self, request):
    #     print(request.data)
    #     try:
    #         authe.send_password_reset_email(request.data['email'])
    #     except:
    #         return Response({"error": "Invalid email"}, status=status.HTTP_400_BAD_REQUEST)
        
    #     account = auth.get_user_by_email(request.data['email'])
    #     new_password = account
        
    #     user = Account.objects.get(email=request.account.email)
    #     if not user.check_password(new_password):
    #         user.set_password(new_password)
    #         user.save()
        
    #     return Response({"message": "Reset password email sent"}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            account = Account.objects.get(email=request.user.email)
            serializer = ChangePasswordSerializer(data=request.data)
            uid = auth.get_user_by_email(request.user.email).uid

            if serializer.is_valid():
                if not account.check_password(serializer.validated_data['old_password']):
                    return Response({"error": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)
                
                account.set_password(serializer.validated_data['new_password'])
                account.save()
                user = auth.update_user(uid, password=serializer.validated_data['new_password'])

                return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "User hasn't login"}, status=status.HTTP_400_BAD_REQUEST)
