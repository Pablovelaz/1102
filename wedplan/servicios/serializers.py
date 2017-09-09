from rest_framework import serializers
from .models import *

class ServiciosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicios
        fields = ('nombre','unidad','costo_u')
