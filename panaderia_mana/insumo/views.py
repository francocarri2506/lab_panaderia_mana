from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumo
from .forms import InsumoForm

def lista_insumos(request):
    insumos = Insumo.objects.all()  # Obtén los insumos desde la base de datos
    return render(request, 'insumo/lista_insumos.html', {'insumos': insumos})

def agregar_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_insumos')
    else:
        form = InsumoForm()
    return render(request, 'insumo/agregar_insumos.html', {'form': form})


def editar_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, id=insumo_id)
    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('lista_insumos')
    else:
        form = InsumoForm(instance=insumo)
    #return render(request, 'insumo/editar_insumo.html', {'form': form})
# Agrega el insumo al contexto para pasarlo a la plantilla
    return render(request, 'insumo/editar_insumo.html', {'form': form, 'insumo': insumo})




def eliminar_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, id=insumo_id)
    insumo.delete()
    return redirect('lista_insumos')



def pagina_inicio(request):
    return render(request, 'inicio.html')  # Renderiza la plantilla 'inicio.html'