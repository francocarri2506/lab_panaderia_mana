
from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_insumos, name='lista_insumos'),
    path('agregar/', views.agregar_insumo, name='agregar_insumo'),
]
