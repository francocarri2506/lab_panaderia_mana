from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, DetallePedido, Insumo
from .forms import PedidoForm

from django.shortcuts import redirect
from django.contrib import messages
from .forms import PedidoForm, DetallePedidoFormSet

@login_required(login_url='usuario:login')
def listar_pedidos(request):
    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()
    context = {
        'pedidos': pedidos
    }
    return render(request, 'pedido/listar_pedidos.html', context)
@login_required(login_url='usuario:login')
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
            #return redirect('pedido_exitoso')
            return redirect('pedido:listar_pedidos')
    else:
        pedido_form = PedidoForm()

    insumos = Insumo.objects.all()
    context = {
        'pedido_form': pedido_form,
        'insumos': insumos,
    }
    #return render(request, 'registrar_pedido.html', context)
    return render(request, 'pedido/registrar_pedido.html', context)

@login_required(login_url='usuario:login')
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
@login_required(login_url='usuario:login')
def eliminar_pedido(request, pedido_id):
    # Obtener el pedido por su ID y eliminarlo
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    messages.success(request, 'Pedido eliminado correctamente.')
    # Redirigir a la lista de pedidos
    return redirect('pedido:listar_pedidos')


"""def editar_pedido(request, pedido_id):
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
    return render(request, 'pedido/editar_pedido.html', context)"""

@login_required(login_url='usuario:login')
def editar_pedido(request, pedido_id):
    # Obtener el pedido y sus detalles
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST, instance=pedido)

        if pedido_form.is_valid():
            pedido = pedido_form.save()

            # Eliminar detalles previos para reemplazarlos con los nuevos
            detalles.delete()

            # Procesar los nuevos detalles del pedido
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

            messages.success(request, 'Pedido actualizado correctamente.')
            return redirect('pedido:listar_pedidos')
    else:
        pedido_form = PedidoForm(instance=pedido)

    insumos = Insumo.objects.all()
    context = {
        'pedido_form': pedido_form,
        'detalles': detalles,
        'pedido': pedido,
        'insumos': insumos,
    }
    return render(request, 'pedido/editar_pedido.html', context)



#reportes

@login_required(login_url='usuario:login')
def lista_reportes(request):
    return render(request, 'pedido/lista_reportes.html')


#1. Vista para Insumos Más Pedidos en PDF

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import DetallePedido

@login_required(login_url='usuario:login')
def insumos_mas_pedidos_pdf(request):

    # Configurar la respuesta para ver el PDF en el navegador
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="insumos_mas_pedidos.pdf"'  # 'inline' para mostrar primero y luego recien descargarlo

    # Crear el archivo PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setTitle("Informe de Insumos Más Pedidos")

    # Título del documento
    p.drawString(100, 800, "Panadería El Maná")
    p.drawString(100, 780, "Informe de Insumos Más Pedidos")

    # Encabezados de la tabla
    p.drawString(100, 750, "Nombre del Insumo")
    p.drawString(300, 750, "Total Pedido")

    # Consultamos los insumos más pedidos
    insumos_mas_pedidos = (DetallePedido.objects
                           .values('insumo__nombre')
                           .annotate(total_pedido=Sum('cantidad'))
                           .order_by('-total_pedido'))

    # Agregar datos a la tabla
    y = 730  # Coordenada vertical inicial para los datos
    for insumo in insumos_mas_pedidos:
        p.drawString(100, y, insumo['insumo__nombre'])
        p.drawString(300, y, str(insumo['total_pedido']))
        y -= 20

    # Finalizar y guardar el PDF
    p.showPage()
    p.save()

    # Obtener contenido del PDF y escribirlo en la respuesta
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response