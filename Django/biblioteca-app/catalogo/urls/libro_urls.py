from django.urls import path
from catalogo.views.libro_views import create_libro, libro_list, update_libro, delete_libro

urlpatterns = [
    path('libros/', libro_list, name='libro_list'),
    path('libros/crear/', create_libro, name='create_libro'),
    path('libros/<int:pk>/editar/', update_libro, name='update_libro'),
    path('libros/<int:pk>/eliminar/', delete_libro, name='delete_libro'),
]