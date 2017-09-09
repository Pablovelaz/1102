from rest_framework import serializers
from .models import *

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ('nombre','tel','email','face')
