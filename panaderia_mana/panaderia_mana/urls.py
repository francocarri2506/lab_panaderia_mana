"""
URL configuration for panaderia_mana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from insumo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insumos/', include('insumo.urls')),
    path('', views.pagina_inicio, name='pagina_inicio'),  # Ruta para la página de inicio
    #path('', TemplateView.as_view(template_name='base/home.html'), name='home'),
    #path('', include('apps.usuario.urls', namespace='usuario')),
    path('productos/', include('producto.urls')),
    path('empleado/', include('empleado.urls')),
    path('cliente/', include('cliente.urls')),
    path('usuario/', include('apps.usuario.urls')),


                  # path('', views.index, name='index'),  # Ruta para la página de inicio
    # path('registro-pedidos/', views.registro_pedidos, name='registro_pedidos'),  # Ruta para Registro de Pedidos
    #path('gestion-producto/', views.gestion_producto, name='gestion_producto'),  # Ruta para Gestión de Productos
    #path('ventas/', views.ventas, name='ventas'),  # Ruta para Ventas

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)