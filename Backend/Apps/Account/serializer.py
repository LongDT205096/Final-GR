from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=256)

    class Meta:
        model = Account
        fields = ['email', 'password']
