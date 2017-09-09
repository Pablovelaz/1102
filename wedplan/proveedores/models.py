from django.db import models
from eventos.models import Evento

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tel = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True, max_length=100)
    pagina = models.URLField(blank=True)
    giro = models.CharField(max_length=100)
    event = models.ManyToManyField(Evento, blank=True, related_name='prov')

    class Meta:
        ordering = ("giro",)

    def __str__(self):
        return "Proveedor %s de %s" % (self.nombre,self.giro)
