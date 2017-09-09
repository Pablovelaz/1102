from django.db import models
from tarea.models import Tarea

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    coment = models.TextField(blank=True)
    tar = models.ForeignKey(Tarea, null=True, related_name='coment')

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "Comentario %s" % (self.coment)
