from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)
        

def register(request):
    """Registro"""
    return HttpResponse("Registro de usuarios")

def sobre_nosotros(request):
    """Desarrollador"""
    return HttpResponse("Estas ante un <h1>gran desarrollador<h1>")

def greeting(request, nombre):
    """Registro de usuarios"""
    return HttpResponse(f"Hola, {nombre}, bienvenido")

def destination(request, titulo, nombre, cargo):
    """Registro de usuarios"""
    return HttpResponse(
        f"Bienvenido:{titulo} {nombre}, su cargo es {cargo}")

def area(request, base, altura):
    """Triangulo"""
    return HttpResponse(
        f"El area del triangiulo:{base*altura/2}")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-firts-template.html", contexto)

def leads_like(request):
    contexto = {
        "titulo": "Programador",
        "nombre": "Daniela Alejandra",
        "apellido": "Melo Villegas"
    }
    return render(request, "leads/leads_like.html", contexto)