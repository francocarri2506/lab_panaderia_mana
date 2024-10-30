from django.urls import path
from venta import views


urlpatterns = [
    path('lista_productos', views.lista_productos, name='lista_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

    path('lista_clientes', views.listar_clientes, name='listar_clientes'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('lista_ventas', views.lista_ventas, name='lista_ventas'),
    path('registrar_venta', views.registrar_venta, name='registrar_venta'),
    path('eliminar_venta/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    #path('nueva_venta', views.AgregarItem.as_view(), name='nueva_venta'),
]