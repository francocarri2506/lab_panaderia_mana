# apps/empleado/views.py
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado
from .forms import EmpleadoForm

@login_required(login_url='usuario:login')
@permission_required('empleado.view_empleado',raise_exception=True)
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/listar_empleados.html', {'empleados': empleados})

@login_required(login_url='usuario:login')
@permission_required('empleado.add_empleado',raise_exception=True)
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/crear_empleado.html', {'form': form})

@login_required(login_url='usuario:login')
@permission_required('empleado.change_empleado',raise_exception=True)
def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/editar_empleado.html', {'form': form})

@login_required(login_url='usuario:login')
@permission_required('empleado.delete_empleado',raise_exception=True)
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    empleado.delete()
    return redirect('listar_empleados')
