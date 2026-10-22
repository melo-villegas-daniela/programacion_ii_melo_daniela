from django.contrib import admin
from .models import Project, Inmuebles

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Inmuebles)
class InmueblesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo_inmueble", "ubicacion", "created_at")
    search_fields = ("nombre", "tipo_inmueble", "ubicacion", "created_at")