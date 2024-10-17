# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro_pedidos(request):
    return render(request, 'registroPedidos.html')

def gestion_producto(request):
    return render(request, 'gestionProducto.html')

def ventas(request):
    return render(request, 'ventas.html')