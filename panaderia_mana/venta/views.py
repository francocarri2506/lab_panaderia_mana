from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView

from .forms import ProductoForm, ItemForm
from .models import Producto
from .models import ClienteMayorista
from .forms import ClienteMayoristaForm
from .models import Venta
from .forms import VentaForm
from django.forms import formset_factory


# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return  render(request, 'producto/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'producto/agregar_producto.html', {'form': form})

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

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos')

def pagina_inicio(request):
    return render(request, 'inicio.html')  # Renderiza la plantilla 'inicio.html'

def listar_clientes(request):
    clientes = ClienteMayorista.objects.all()
    return render(request, 'cliente/listar_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteMayoristaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteMayoristaForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})

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

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteMayorista, id=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/lista_ventas.html',{'ventas': ventas})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'venta/registrar_venta.html', {'form': form})

def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    venta.delete()
    return redirect('lista_ventas')

class AgregarItem(FormView):
    template_name = 'venta/nueva_venta.html'
    form_class = formset_factory(ItemForm)
    
    def form_valid(self, form):
        for f in form:
            f.save()

        return super(AgregarItem, self).form_valid(form)

def eliminar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()