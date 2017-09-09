from django.contrib import admin
from .models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comentario, ComentarioAdmin)
