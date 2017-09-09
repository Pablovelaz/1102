from rest_framework import serializers
from .models import *

class TipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo
        fields = ('nombre',)
