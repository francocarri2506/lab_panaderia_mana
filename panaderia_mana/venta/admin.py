from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Producto)
class Producto(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'cantidadDisponible', 'tipo', 'unidadMedida']
    search_fields = ('nombre', 'tipo')

@admin.register(ClienteMayorista)
class ClienteMayorista(admin.ModelAdmin):
    list_display = ['cuit', 'nombreCompleto']
    search_fields = ('cuit', 'nombreCompleto','domicilioCalle')

@admin.register(Venta)
class Venta(admin.ModelAdmin):
    list_display = ['fechaVenta', 'tipoVenta', 'montoTotal', 'empleadoVenta']
    search_fields = ('fechaVenta', 'tipoVenta')

@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ['prod', 'venta', 'cantidad', 'subTotal']
    search_fields = ('prod', 'SubTotal')
