from rest_framework import serializers
from .models import *
from tipos.serializers import TipoSerializer

class SubTareaSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer(many=True)

    class Meta:
        model = SubTarea
        fields = ('nombre','fcreacion','fplaneado','completado','tipo')
