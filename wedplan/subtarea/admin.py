from django.contrib import admin
from .models import SubTarea

class SubTareaAdmin(admin.ModelAdmin):
    pass

admin.site.register(SubTarea, SubTareaAdmin)
