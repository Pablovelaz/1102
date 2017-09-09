from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tarea, TareaAdmin)
