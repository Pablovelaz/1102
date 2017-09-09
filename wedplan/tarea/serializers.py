from rest_framework import serializers
from .models import *
from subtarea.serializers import SubTareaSerializer
from comentarios.serializers import ComentarioSerializer

class TareaSerializer(serializers.ModelSerializer):
    sub_tarea = SubTareaSerializer(many=True)
    coment = ComentarioSerializer(many=True)
    class Meta:
        model = Tarea
        fields = ('nombre','fcreacion','fplaneado','completado','sub_tarea','coment')
