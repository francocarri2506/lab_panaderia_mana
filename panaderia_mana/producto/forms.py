from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','cantidadDisponible','unidadMedida','tipo','imagen',]
        #widgets = {
        #    'imagen': forms.ClearableFileInput(),}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-faded', 'aria-describedby': 'basic-addon1'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-faded', 'rows': 3, 'aria-describedby': 'basic-addon2'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control bg-faded', 'aria-describedby': 'basic-addon3'}),
            'cantidadDisponible': forms.NumberInput(attrs={'class': 'form-control bg-faded', 'aria-describedby': 'basic-addon4'}),
            'unidadMedida': forms.TextInput(attrs={'class': 'form-control bg-faded', 'aria-describedby': 'basic-addon5'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control bg-faded', 'aria-describedby': 'basic-addon6'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control bg-faded', 'aria-describedby': 'basic-addon7'}),
        }
