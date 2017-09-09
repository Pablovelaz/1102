from django.db import models
from proveedores.models import Proveedor

class Servicios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100,blank=True)
    costo_u = models.IntegerField()
    prov = models.ManyToManyField(Proveedor, blank=True, related_name='serv')

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "Servicio: %s" % (self.nombre)
