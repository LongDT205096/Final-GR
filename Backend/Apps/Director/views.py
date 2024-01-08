from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import Director
from .serializer import DirectorSerializer


class DirectorDetailView(APIView):
    def get(self, request, pk):
        director = Director.objects.get(pk=pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
