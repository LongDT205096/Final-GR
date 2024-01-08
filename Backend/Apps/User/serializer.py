from rest_framework import serializers
from .models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_field = ('account')
        required_fields = ('first_name', 'last_name')
