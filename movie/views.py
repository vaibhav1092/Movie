from django.shortcuts import render

# Create your views here.
from .models import Actor,Movie
from .serializers import Movieseriliazer,Actorseriliazer
from rest_framework.viewsets import ModelViewSet


class MovieActions(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movieseriliazer


class ActorActions(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = Actorseriliazer