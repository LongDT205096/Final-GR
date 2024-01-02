from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from .models import User, Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = User
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=4, max_length=256, write_only=True)
    re_enter_password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ("username", "password", "re_enter_password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, username):
        try:
            Account.objects.get(username=username)
        except Account.DoesNotExist:
            return username
            
        raise ValidationError({"success": False, "msg": "Username already existed."})


    def create(self, validated_data):
        if validated_data["password"] != validated_data["re_enter_password"]:
            raise ValidationError(
                {"success": False, "msg": "Password does not match."}
            )
            
        return Account.objects.create_user(
            validated_data["username"], validated_data["password"]
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=256, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        
        if username and password:
            try:
                account = Account.objects.get(username=username)
            except Account.DoesNotExist:
                raise ValidationError(
                    {"success": False, "msg": "Username does not exist."}
                )
            
            if account.check_password(password):
                if not account.is_active:
                    raise ValidationError(
                        {"success": False, "msg": "User is not active"}
                    )

                return {
                    "success": True,
                    "user": {"_id": account.id},
                }
            
            else:
                raise ValidationError({"success": False, "msg": "Wrong password"})
                
        else:
            raise ValidationError(
                {"success": False, "msg": "Must provide username and password."}
            )


