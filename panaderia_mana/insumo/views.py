from django.shortcuts import render, redirect
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




def pagina_inicio(request):
    return render(request, 'inicio.html')  # Renderiza la plantilla 'inicio.html'