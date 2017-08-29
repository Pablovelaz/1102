from django.db import models
from user.models import User
import datetime

def user_directory_path(instance,filename):
    #Va subir la imagene en el media root de cada usuario
    return 'user_{0}/{1}'.format(instance.usuario.id,filename)

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    orden = models.URLField(blank=True)
    num_inv = models.IntegerField(blank=True)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=300)
    croquis = models.ImageField(upload_to = user_directory_path,blank=True)
    usuario = models.ForeignKey(User, blank=True,null=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "Evento %s" % (self.nombre)
