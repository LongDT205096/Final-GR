from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=256)

    class Meta:
        model = Account
        fields = ['email', 'password']

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=256)
    new_password = serializers.CharField(max_length=256)

    class Meta:
        model = Account
        fields = ['old_password', 'new_password']
