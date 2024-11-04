
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .forms import ProductoForm, ItemForm, ItemFormSet
from .models import Producto, Item
from .models import ClienteMayorista
from .forms import ClienteMayoristaForm
from .models import Venta
from .forms import VentaForm
from django.forms import formset_factory

from empleado.models import Empleado

items = []

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return  render(request, 'producto/lista_productos.html', {'productos': productos})

@login_required(login_url='usuario:login')
def lista_productos(request):
    productos = Producto.objects.all()
    return  render(request, 'producto/lista_productos2.html', {'productos': productos})
"""
@login_required(login_url='usuario:login')
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'producto/agregar_producto.html', {'form': form})
"""
@login_required(login_url='usuario:login')
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  # incluir request.FILES para las imagenes
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'producto/agregar_producto.html', {'form': form})



@login_required(login_url='usuario:login')
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'producto/editar_producto.html', {'form': form, 'producto': producto})

@login_required(login_url='usuario:login')
@permission_required('venta.delete_producto',raise_exception=True)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos')

def pagina_inicio(request):
    return render(request, 'inicio.html')  # Renderiza la plantilla 'inicio.html'

@login_required(login_url='usuario:login')
def listar_clientes(request):
    clientes = ClienteMayorista.objects.all()
    return render(request, 'cliente/listar_clientes.html', {'clientes': clientes})

@login_required(login_url='usuario:login')
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteMayoristaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteMayoristaForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})

@login_required(login_url='usuario:login')
@permission_required('venta.change_clienteMayorista',raise_exception=True)
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteMayorista, id=cliente_id)
    if request.method == 'POST':
        form = ClienteMayoristaForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteMayoristaForm(instance=cliente)
    return render(request, 'cliente/editar_cliente.html', {'form': form, 'cliente': cliente})

@login_required(login_url='usuario:login')
@permission_required('venta.delete_clienteMayorista',raise_exception=True)
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteMayorista, id=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')

@login_required(login_url='usuario:login')
def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/lista_ventas.html',{'ventas': ventas})

@login_required(login_url='usuario:login')
def registrar_venta(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            total = 0
            venta = venta_form.save(commit=False)
            items_ids = request.POST.getlist('producto_id[]')
            cantidades = request.POST.getlist('cantidad[]')
            for item_id, cantidad in zip(items_ids, cantidades):
                item = Producto.objects.get(id=item_id)
                if item.unidadMedida == "GR":
                    total+= (item.precio * int(cantidad)/1000)
                else:
                    total+= (item.precio * int(cantidad))

            venta.tipoVenta = venta.tipoCliente
            venta.montoTotal = total
            usuario = request.user
            empleado = get_object_or_404(Empleado, usuario=usuario)
            venta.empleadoVenta = empleado
            venta.save()
            for item_id, cantidad in zip(items_ids, cantidades):
                item = Producto.objects.get(id=item_id)
                item.venta(int(cantidad))
                Item.objects.create(
                    prod=item,
                    venta=venta,
                    cantidad=cantidad,
                    subTotal=item.precio * int(cantidad)
                )



            messages.success(request, 'Venta registrada exitosamente.')
            return redirect('lista_ventas')
    else:
        venta_form = VentaForm()
    productos = Producto.objects.all()
    context = {
        'venta_form': venta_form,
        'productos': productos,
    }
    return render(request, 'venta/registrar_venta.html', context)

"""def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        total=0
        formset = ItemFormSet(request.POST, instance=venta)
        if formset.is_valid():
        if form.is_valid():
            for i in items:
                total += i.subTotal

            venta = form.save(commit=False)
            venta.montoTotal = total
            venta.save()
            for i in items:
                i.venta = venta
                producto = get_object_or_404(Producto, id=i.prod)
                producto.venta(i.cantidad)
                i.save()
            for f in formset:
                    producto = get_object_or_404(Producto, nombre=f.cleaned_data['prod'])
                    itemV = f.save(commit=False)
                    itemV.subTotal = float(producto.precio) * int(f.cleaned_data['cantidad'])
                    total += itemV.subTotal
                    items.append(itemV)


            for i in items:
                    i.venta = venta
                    producto = get_object_or_404(Producto, nombre=i.prod)
                    producto.venta(i.cantidad)
                    i.save()

                for i in items:
                    items.remove(i)

            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'venta/registrar_venta.html', {'form': form})"""

@login_required(login_url='usuario:login')
@permission_required('venta.delete_venta',raise_exception=True)
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    venta.delete()
    return redirect('lista_ventas')

"""
class AgregarItem(FormView):
    template_name = 'venta/nueva_venta.html'
    form_class = formset_factory(ItemForm)
    success_url = 'registrar_venta'


    def form_valid(self, form):

        for f in form:
            producto = get_object_or_404(Producto,nombre=f.cleaned_data['prod'])
            itemV = f.save(commit=False)
            itemV.subTotal = float(producto.precio) * int(f.cleaned_data['cantidad'])
            items.append(itemV)


        redirect('registrar_venta')
        return super(AgregarItem, self).form_valid(form)
"""
@login_required(login_url='usuario:login')
def eliminar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()


@login_required(login_url='usuario:login')
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto/detalle_producto.html', {'producto': producto})


from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, F, Count
from .models import Venta, Item, Producto
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

@login_required(login_url='usuario:login')
def informe_ventas_pdf(request, tipo=None, fecha_inicio=None, fecha_fin=None):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="informe_ventas.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    # Título del informe
    p.drawString(100, 800, "Listado de Ventas")
    y = 780

    # Aplicar filtros de rango de fechas y tipo de producto
    ventas = Venta.objects.all()

    # Filtrar por rango de fechas si se proporcionan
    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fechaVenta__range=[fecha_inicio, fecha_fin])

    # Filtrar por tipo de producto si se proporciona
    if tipo:
        ventas = ventas.filter(item__prod__tipo=tipo)

    # Iterar sobre las ventas para mostrar cada venta y sus productos
    if ventas.exists():
        for venta in ventas:
            items = Item.objects.filter(venta=venta)

            # Mostrar detalles de la venta
            p.drawString(100, y, f"Fecha de Venta: {venta.fechaVenta} - Monto Total: {venta.montoTotal}")
            y -= 20

            # Mostrar cada producto vendido en la venta
            for item in items:
                p.drawString(120, y,
                             f"Producto: {item.prod.nombre}, Cantidad: {item.cantidad}, Subtotal: {item.subTotal}")
                y -= 20

            y -= 10  # Espacio extra después de cada venta

            # Crear una nueva página si la longitud se pasa del límite
            if y < 50:
                p.showPage()
                y = 800
    else:
        p.drawString(100, y, "No se encontraron ventas para los filtros aplicados.")

    # Guardar y devolver el PDF
    p.showPage()
    p.save()
    response.write(buffer.getvalue())
    buffer.close()
    return response

#3. Listado de Empleados con Más Ventas
@login_required(login_url='usuario:login')
def empleados_mas_ventas_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="empleados_mas_ventas.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.drawString(100, 800, "Empleados con Más Ventas")

    empleados_mas_ventas = (Venta.objects
                            .values('empleadoVenta__nombreCompleto')
                            .annotate(total_ventas=Count('id'))
                            .order_by('-total_ventas'))

    y = 780
    for empleado in empleados_mas_ventas:
        p.drawString(100, y, f"Empleado: {empleado['empleadoVenta__nombreCompleto']}, Total Ventas: {empleado['total_ventas']}")
        y -= 20

    p.showPage()
    p.save()
    response.write(buffer.getvalue())
    buffer.close()
    return response

#2. Listado de los Productos Más Vendidos

from django.db.models import Sum
@login_required(login_url='usuario:login')
def productos_mas_vendidos_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="productos_mas_vendidos.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.drawString(100, 800, "Productos Más Vendidos")

    productos_mas_vendidos = (Item.objects
                              .values('prod__nombre')
                              .annotate(total_vendido=Sum('cantidad'))
                              .order_by('-total_vendido'))

    y = 780
    for producto in productos_mas_vendidos:
        p.drawString(100, y, f"Producto: {producto['prod__nombre']}, Cantidad Vendida: {producto['total_vendido']}")
        y -= 20

    p.showPage()
    p.save()
    response.write(buffer.getvalue())
    buffer.close()
    return response



from django.utils import timezone
@login_required(login_url='usuario:login')
def ventas_diarias_pdf(request):
    # Configurar la respuesta para ver el PDF en el navegador
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="ventas_diarias.pdf"'

    # Crear el archivo PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setTitle("Informe de Ventas Diarias")

    # Título del documento
    p.drawString(100, 800, "Panadería El Maná")
    p.drawString(100, 780, "Informe de Ventas del Día")

    # Encabezados de la tabla
    p.drawString(100, 750, "Producto")
    p.drawString(300, 750, "Cantidad Vendida")
    p.drawString(400, 750, "Subtotal")

    # Filtramos las ventas del día actual en la zona horaria local
    today = timezone.localdate()
    ventas_hoy = Venta.objects.filter(fechaVenta=today)

    # Verificar si hay ventas hoy
    if ventas_hoy.exists():
        y = 730  # Coordenada vertical inicial para los datos
        total_dia = 0  # Para acumular el total del día

        # Iterar a través de las ventas y sus items
        for venta in ventas_hoy:
            items = Item.objects.filter(venta=venta)
            for item in items:
                p.drawString(100, y, item.prod.nombre)  # Nombre del producto
                p.drawString(300, y, str(item.cantidad))  # Cantidad vendida
                p.drawString(400, y, f"${item.subTotal:.2f}")  # Subtotal
                total_dia += item.subTotal  # Sumar al total del día
                y -= 20

        # Mostrar el total del día
        p.drawString(100, y - 10, f"Total del Día: ${total_dia:.2f}")
    else:
        p.drawString(100, 730, "No se registraron ventas para el día de hoy.")

    # Finalizar y guardar el PDF
    p.showPage()
    p.save()

    # Obtener contenido del PDF y escribirlo en la respuesta
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response