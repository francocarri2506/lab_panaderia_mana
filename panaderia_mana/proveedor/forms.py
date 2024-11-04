from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombreCompleto', 'telefono', 'email', 'domicilioCalle', 'domicilioNumero', 'domicilioLocalidad','domicilioDepartamento']
        widgets = {
            'nombreCompleto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control','required': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'domicilioCalle': forms.TextInput(attrs={'class': 'form-select','required': True}),
            'domicilioNumero': forms.NumberInput(attrs={'class': 'form-control','required': True}),
            'domicilioLocalidad': forms.TextInput(attrs={'class': 'form-select', 'required': True}),
            'domicilioDepartamento': forms.TextInput(attrs={'class': 'form-select', 'required': True}),
        }