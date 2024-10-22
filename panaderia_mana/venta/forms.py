from django import forms
from django.forms import DateInput
from .models import ClienteMayorista
from .models import Producto
from .models import Venta


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidadDisponible', 'unidadMedida', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidadDisponible': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidadMedida': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(),
        }



class ClienteMayoristaForm(forms.ModelForm):
    class Meta:
        model = ClienteMayorista
        fields = '__all__'
        widgets = {
            'cuit': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilioCalle': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilioNumero': forms.NumberInput(attrs={'class': 'form-control'}),
            'domicilioLocalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilioDepartamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields =  ['tipoCliente',  'fechaVenta', 'tipoVenta', 'formaPago', 'tipoComprobante', 'observaciones', 'clienteM']
        widgets = {
            'tipoCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaVenta': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'tipoVenta': forms.TextInput(attrs={'class': 'form-control'}),
            'formaPago': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoComprobante': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'clienteM': forms.Select(),

        }