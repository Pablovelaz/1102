from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^tipo/', include('tipos.urls')),
    url(r'^subtar/', include('subtarea.urls')),
    url(r'^tar/', include('tarea.urls')),
    url(r'^com/', include('comentarios.urls')),
    url(r'^serv/', include('servicios.urls')),
    url(r'^cli/', include('clientes.urls')),
    url(r'^prov/', include('proveedores.urls')),
    url(r'^ev/', include('eventos.urls')),
    url(r'^user/', include('user.urls')),
]
