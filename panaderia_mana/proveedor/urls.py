from django.urls import path
from proveedor import views


urlpatterns = [
    path('lista_proveedores', views.lista_proveedores, name='lista_proveedores'),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('editar_proveedor/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor')

]