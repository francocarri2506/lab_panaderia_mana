from django.contrib import admin
from .models import Empleado
# Register your models here.
@admin.register(Empleado)
class Empleado(admin.ModelAdmin):
    list_display = ['cuit', 'nombreCompleto', 'fechaIncorporacion', 'telefono', 'usuario']
    search_fields = ('nombreCompleto', 'cuit', 'fechaIncorporacion', 'fechaNacimineto', 'telefono')