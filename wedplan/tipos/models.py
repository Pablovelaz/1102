from django.db import models
from subtarea.models import SubTarea

class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    subtar = models.ForeignKey(SubTarea, blank=True,null=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "Tipo %s" % (self.nombre)
