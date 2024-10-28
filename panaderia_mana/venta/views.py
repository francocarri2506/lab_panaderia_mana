from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm, ItemForm, ItemFormSet
from .models import Producto
from .models import ClienteMayorista
from .forms import ClienteMayoristaForm
from .models import Venta
from .forms import VentaForm
from django.forms import formset_factory

items = []

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return  render(request, 'producto/lista_productos.html', {'productos': productos})

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
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            total = 0
            venta = form.save(commit=False)
            formset = ItemFormSet(request.POST, instance=venta)
            if formset.is_valid():
                for f in formset:
                    producto = get_object_or_404(Producto, nombre=f.cleaned_data['prod'])
                    itemV = f.save(commit=False)
                    itemV.subTotal = float(producto.precio) * int(f.cleaned_data['cantidad'])
                    total += itemV.subTotal
                    items.append(itemV)

                venta.montoTotal = total
                venta.save()
                for i in items:
                    i.venta = venta
                    producto = get_object_or_404(Producto, nombre=i.prod)
                    producto.venta(i.cantidad)
                    i.save()

                for i in items:
                    items.remove(i)

                messages.success(request, 'Venta registrada exitosamente.')
                return redirect('lista_ventas')
    else:
        form = VentaForm()
        formset = ItemFormSet()

    return render(request, 'venta/registrar_venta.html', {
        'form': form,
        'formset': formset
    })

"""def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        total=0
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


            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'venta/registrar_venta.html', {'form': form})"""

@login_required(login_url='usuario:login')
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

