from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import Actor
from .serializer import ActorSerializer


class ActorDetailView(APIView):
    def get(self, request, pk):
        actor = Actor.objects.get(pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
