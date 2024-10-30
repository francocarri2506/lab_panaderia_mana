from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.pdfgen import canvas

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


#1. Vista para Insumos Faltantes en PDF
"""
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.db.models import Sum
from .models import Insumo
from django.db.models import F

def insumos_faltantes_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="insumos_faltantes.pdf"'

    p = canvas.Canvas(response)
    #insumos_faltantes = Insumo.objects.filter(cantidad_disponible__lt=models.F('cantidad_minima'))
    insumos_faltantes = Insumo.objects.filter(cantidad_disponible__lt=F('cantidad_minima'))

    p.drawString(100, 750, "Listado de Insumos Faltantes")
    y = 730
    for insumo in insumos_faltantes:
        p.drawString(100, y, f"Insumo: {insumo.nombre}, Cantidad Disponible: {insumo.cantidad_disponible}")
        y -= 20

    p.showPage()
    p.save()
    return response
"""
from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponse
from .models import Insumo
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def insumos_faltantes_pdf(request):
    # Obtén los insumos faltantes (donde la cantidad disponible es menor que la cantidad mínima)
    insumos_faltantes = Insumo.objects.filter(cantidad_disponible__lt=F('cantidad_minima'))

    # Crear un archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="insumos_faltantes.pdf"'

    # Configurar el PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle("Listado de Insumos Faltantes")

    # Agregar título
    pdf.drawString(100, 800, "Listado de Insumos Faltantes")
    pdf.drawString(100, 780, "Panadería El Maná")  # Nombre de la panadería

    # Encabezados de la tabla
    pdf.drawString(100, 750, "Nombre del Insumo")
    pdf.drawString(300, 750, "Cantidad Disponible")
    pdf.drawString(450, 750, "Cantidad Mínima")

    y = 730  # Coordenada vertical inicial para los datos

    # Agregar los datos de los insumos faltantes
    for insumo in insumos_faltantes:
        pdf.drawString(100, y, insumo.nombre)
        pdf.drawString(300, y, str(insumo.cantidad_disponible))
        pdf.drawString(450, y, str(insumo.cantidad_minima))
        y -= 20  # Espacio entre las filas

    pdf.showPage()
    pdf.save()

    # Obtener el contenido del PDF y escribirlo en la respuesta
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response