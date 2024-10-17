from django import forms
from .models import Insumo

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'cantidad_disponible','cantidad_minima']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_minima': forms.NumberInput(attrs={'class': 'form-control'}),
        }