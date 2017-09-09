from django.contrib import admin
from .models import Tipo

class TipoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tipo, TipoAdmin)
