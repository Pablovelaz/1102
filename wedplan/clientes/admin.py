from django.contrib import admin
from .models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Clientes, ClientesAdmin)
