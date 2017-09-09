from django.db import models
from eventos.models import Evento

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tel = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True, max_length=100)
    face = models.URLField(unique=True, max_length=500, blank=True, null=True)
    event = models.ForeignKey(Evento,null=True, related_name='client')

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "Persona: %s" % (self.nombre)
