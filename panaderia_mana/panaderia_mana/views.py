# views.py

from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ItemForm


def index(request):
    return render(request, 'index.html')

def registro_pedidos(request):
    return render(request, 'registroPedidos.html')

def gestion_producto(request):
    return render(request, 'gestionProducto.html')

def ventas(request):
    return render(request, 'ventas.html')

class registrar_venta(FormView):
    template_name = 'venta/registar_venta.html'
    form_class = ItemForm
    success_url = ''