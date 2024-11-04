"""

# pedido/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('<int:pedido_id>/agregar-items/', views.agregar_items_pedido, name='agregar_items_pedido'),
]
"""

# urls.py
from django.urls import path
from .views import registrar_pedido
from . import views
app_name = 'pedido'
urlpatterns = [
    path('registrar-pedido/', registrar_pedido, name='registrar_pedido'),
    path('', views.listar_pedidos, name='listar_pedidos'),
    path('pedido/<int:pedido_id>/', views.detalles_pedido, name='detalles_pedido'),
    path('<int:pedido_id>/eliminar/', views.eliminar_pedido, name='eliminar_pedido'),
    path('<int:pedido_id>/editar/', views.editar_pedido, name='editar_pedido'),


    path('insumos-mas-pedidos/pdf/', views.insumos_mas_pedidos_pdf, name='insumos_mas_pedidos_pdf'),

    path('lista-reportes/', views.lista_reportes, name='lista_reportes'),
]