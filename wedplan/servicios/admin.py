from django.contrib import admin
from .models import Servicios

class ServiciosAdmin(admin.ModelAdmin):
    pass

admin.site.register(Servicios, ServiciosAdmin)
