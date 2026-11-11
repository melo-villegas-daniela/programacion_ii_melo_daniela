
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('catalogo.urls.home_urls')),
    path('admin/', admin.site.urls),
    path('catalogo/categorias/', include('catalogo.urls.categoria_urls')),
    path('catalogo/', include('catalogo.urls.libro_urls')),
    path('cuentas/', include('catalogo.urls.authentication_urls')),
]
