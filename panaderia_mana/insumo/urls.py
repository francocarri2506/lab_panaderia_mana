
from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_insumos, name='lista_insumos'),
    path('agregar/', views.agregar_insumo, name='agregar_insumo'),
    path('editar/<int:insumo_id>/', views.editar_insumo, name='editar_insumo'),
    path('eliminar/<int:insumo_id>/', views.eliminar_insumo, name='eliminar_insumo'),

]
