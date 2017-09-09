from rest_framework import serializers
from .models import *
from servicios.serializers import ServiciosSerializer
from tarea.serializers import TareaSerializer

class ProveedorSerializer(serializers.ModelSerializer):
    tarea = TareaSerializer(many=True)
    serv = ServiciosSerializer(many=True)
    class Meta:
        model = Proveedor
        fields = ('nombre','tel','email','pagina','giro','tarea','serv')
