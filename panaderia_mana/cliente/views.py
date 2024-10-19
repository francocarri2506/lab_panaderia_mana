# apps/cliente/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import ClienteMayorista
from .forms import ClienteMayoristaForm

def listar_clientes(request):
    clientes = ClienteMayorista.objects.all()
    return render(request, 'cliente/listar_usuario.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteMayoristaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteMayoristaForm()
    return render(request, 'cliente/crear_usuario.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteMayorista, id=cliente_id)
    if request.method == 'POST':
        form = ClienteMayoristaForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteMayoristaForm(instance=cliente)
    return render(request, 'cliente/editar_usuario.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteMayorista, id=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')
