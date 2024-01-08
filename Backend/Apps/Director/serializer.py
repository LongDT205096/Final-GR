from rest_framework.serializers import ModelSerializer
from .models import Director

class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
