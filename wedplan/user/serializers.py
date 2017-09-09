from rest_framework import serializers
from .models import *
from eventos.serializers import EventoSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nombre')

class UserDetSerializer(serializers.ModelSerializer):
    event = EventoSerializer(many=True)
    class Meta:
        model = User
        fields = ('nombre','apellidos','email','event')
