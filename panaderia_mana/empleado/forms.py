# apps/empleado/forms.py

from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'cuit': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fechaIncorporacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'domicilioCalle': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilioNumero': forms.NumberInput(attrs={'class': 'form-control'}),
            'domicilioLocalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilioDepartamento': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }