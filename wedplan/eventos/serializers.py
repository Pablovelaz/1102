from rest_framework import serializers
from .models import *
from clientes.serializers import ClientesSerializer
from proveedores.serializers import ProveedorSerializer

class EventoSerializer(serializers.ModelSerializer):
    client = ClientesSerializer(many=True)
    prov = ProveedorSerializer(many=True)
    class Meta:
        model = Evento
        fields = ('nombre','orden','num_inv','fecha','lugar','croquis','client','prov')
