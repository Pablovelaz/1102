from django.db import models
from proveedores.models import Proveedor
import datetime

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fcreacion = models.DateTimeField(auto_now_add=True)
    fplaneado = models.DateTimeField()
    fcompletado = models.DateTimeField(null=True,blank=True)
    completado = models.BooleanField(default=False)
    prov = models.ManyToManyField(Proveedor, blank=True)

    class Meta:
        ordering = ("fplaneado",)

    def __str__(self):
        return "Tarea %s" % (self.nombre)
