
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, DetallePedido, Insumo
from .forms import PedidoForm

from django.shortcuts import redirect
from django.contrib import messages
from .forms import PedidoForm, DetallePedidoFormSet

def listar_pedidos(request):
    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()
    context = {
        'pedidos': pedidos
    }
    return render(request, 'pedido/listar_pedidos.html', context)

def registrar_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)

        if pedido_form.is_valid():
            pedido = pedido_form.save()
            # Procesar los detalles del pedido
            insumo_ids = request.POST.getlist('insumo_id[]')
            cantidades = request.POST.getlist('cantidad[]')

            for insumo_id, cantidad in zip(insumo_ids, cantidades):
                insumo = Insumo.objects.get(id=insumo_id)
                DetallePedido.objects.create(
                    pedido=pedido,
                    insumo=insumo,
                    cantidad=cantidad,
                    precio_total=insumo.precio_unitario * int(cantidad)
                )
            return redirect('pedido_exitoso')
        # return redirect('listar_pedidos')
    else:
        pedido_form = PedidoForm()

    insumos = Insumo.objects.all()
    context = {
        'pedido_form': pedido_form,
        'insumos': insumos,
    }
    #return render(request, 'registrar_pedido.html', context)
    return render(request, 'pedido/registrar_pedido.html', context)


def detalles_pedido(request, pedido_id):
    # Obtener el pedido por su ID
    pedido = get_object_or_404(Pedido, id=pedido_id)
    # Obtener los detalles asociados al pedido
    detalles = DetallePedido.objects.filter(pedido=pedido)
    context = {
        'pedido': pedido,
        'detalles': detalles
    }
    return render(request, 'pedido/detalles_pedido.html', context)

"""
def detalles_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedido/detalles_pedido.html', {'pedido': pedido})
"""
def eliminar_pedido(request, pedido_id):
    # Obtener el pedido por su ID y eliminarlo
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    messages.success(request, 'Pedido eliminado correctamente.')
    # Redirigir a la lista de pedidos
    return redirect('pedido/listar_pedidos.html')


def editar_pedido(request, pedido_id):
    # Obtener el pedido y sus detalles
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST, instance=pedido)
        detalle_formset = DetallePedidoFormSet(request.POST, queryset=detalles)

        if pedido_form.is_valid() and detalle_formset.is_valid():
            pedido_form.save()
            detalle_formset.save()
            messages.success(request, 'Pedido actualizado correctamente.')
            return redirect('pedido/listar_pedidos.html')
    else:
        pedido_form = PedidoForm(instance=pedido)
        detalle_formset = DetallePedidoFormSet(queryset=detalles)

    context = {
        'pedido_form': pedido_form,
        'detalle_formset': detalle_formset,
        'pedido': pedido
    }
    return render(request, 'pedido/editar_pedido.html', context)