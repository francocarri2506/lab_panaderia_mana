from django import forms
from django.forms import DateInput, inlineformset_factory
from .models import ClienteMayorista
from .models import Producto
from .models import Venta
from .models import Item


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidadDisponible', 'unidadMedida', 'tipo','imagen',]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control','required': True}),
            'cantidadDisponible': forms.NumberInput(attrs={'class': 'form-control','required': True}),
            'unidadMedida': forms.Select(attrs={'class': 'form-select','required': True}),
            'tipo': forms.Select(attrs={'class': 'form-select','required': True}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control bg-faded', 'aria-describedby': 'basic-addon7'}),
        }

class ClienteMayoristaForm(forms.ModelForm):
    class Meta:
        model = ClienteMayorista
        fields = '__all__'
        widgets = {
            'cuit': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nombreCompleto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'domicilioCalle': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'domicilioNumero': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'domicilioLocalidad': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'domicilioDepartamento': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields =  ['tipoCliente',  'fechaVenta', 'formaPago', 'tipoComprobante', 'observaciones', 'clienteM']
        widgets = {
            'tipoCliente': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'fechaVenta': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'required': True}),
            #'tipoVenta': forms.TextInput(attrs={'class': 'form-control'}),
            'formaPago': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'tipoComprobante': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'clienteM': forms.Select(attrs={'class': 'form-select'}),

        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['prod', 'cantidad']
        widgets = {
            'prod': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'})
        }

ItemFormSet = inlineformset_factory(
    Venta,
    Item,
    form=ItemForm,
    extra=1,  # Número de formularios vacíos
    can_delete=True  # Permite eliminar
)
