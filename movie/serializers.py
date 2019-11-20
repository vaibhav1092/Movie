from rest_framework.serializers import ModelSerializer
from .models import Movie,Actor



class Actorseriliazer(ModelSerializer):
    # Movi_Act = ModelSerializer(many=True)

    class Meta:
        model= Actor
        fields= '__all__'




class Movieseriliazer(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

