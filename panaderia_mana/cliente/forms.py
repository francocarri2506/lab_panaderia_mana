# apps/cliente/forms.py

from django import forms
from .models import ClienteMayorista

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