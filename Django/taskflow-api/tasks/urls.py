from django.urls import path
from . import views

app_name = "tasks"   

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("sobre_nosotros/", views.sobre_nosotros, name="sobre_nosotros"),
    path("greeting/<str:nombre>", views.greeting, name="greeting"),
    path("destinatario/<str:titulo>/<str:nombre>/<str:cargo>", views.destination, name="destinatario"),
    path("area_triangulo/<int:base>/<int:altura>", views.area, name="area_triangulo"),
    path("my-first-template", views.my_first_template, name="my-first-template"),
]