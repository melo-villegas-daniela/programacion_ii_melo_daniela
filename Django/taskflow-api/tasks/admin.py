from django.contrib import admin
from .models import Project, Inmuebles, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Inmuebles)
class InmueblesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo_inmueble", "ubicacion", "created_at")
    search_fields = ("nombre", "tipo_inmueble", "ubicacion", "created_at")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")