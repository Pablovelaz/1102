from django.db import models
from tarea.models import Tarea
import datetime

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fcreacion = models.DateTimeField(auto_now_add=True)
    fplaneado = models.DateTimeField()
    fcompletado = models.DateTimeField(null=True,blank=True)
    completado = models.BooleanField(default=False)
    tar = models.ForeignKey(Tarea, null=True, related_name='sub_tarea')

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "SubTarea %s" % (self.nombre)
