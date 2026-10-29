
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ProjectForm, TaskForm
from .models import Project


def home(request):
    return render(request, "tasks/home.html", {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    })


def register(request):
    return HttpResponse("Registro de usuarios")


def sobre_nosotros(request):
    return HttpResponse(
        "<h1>Estás ante un gran desarrollador</h1>"
    )


def greeting(request, nombre):
    return HttpResponse(f"Hola, {nombre}, bienvenido")


def destination(request, titulo, nombre, cargo):
    return HttpResponse(
        f"Bienvenido: {titulo} {nombre}, su cargo es {cargo}"
    )


def area(request, base, altura):
    return HttpResponse(
        f"El área del triángulo: {base * altura / 2}"
    )


def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(
        request,
        "tasks/my-first-template.html",
        contexto,
    )


def leads_like(request):
    contexto = {
        "titulo": "Programador",
        "nombre": "Daniela Alejandra",
        "apellido": "Melo Villegas",
    }
    return render(request, "leads/leads_like.html", contexto)


def project_list(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "projects/projects.html", contexto)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:project-list")
    else:
        form = TaskForm()

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "modo": "crear"},
    )


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:project-list")
    else:
        form = ProjectForm()

    return render(
        request,
        "projects/project_form.html",
        {"form": form, "modo": "crear"},
    )
