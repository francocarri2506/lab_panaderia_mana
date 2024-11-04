from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import ProveedorForm
from .models import Proveedor

@login_required(login_url='usuario:login')
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return  render(request, 'proveedor/lista_proveedores.html', {'proveedores': proveedores})

@login_required(login_url='usuario:login')
@permission_required('proveedor.add_proveedor',raise_exception=True)
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/agregar_proveedor.html', {'form': form})

@login_required(login_url='usuario:login')
@permission_required('proveedor.change_proveedor',raise_exception=True)
def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'proveedor/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

@login_required(login_url='usuario:login')
@permission_required('proveedor.delete_proveedor',raise_exception=True)
def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.delete()
    return redirect('lista_proveedores')