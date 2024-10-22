from django import forms
from .models import ClienteMayorista
from .models import Producto


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
            #'imagen': forms.ImageField()
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