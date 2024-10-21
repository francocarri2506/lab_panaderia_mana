from django import forms
from .models import Producto, Venta

class ItemForm(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ('nombre',
                  'precio',
                  'tipo',
                  )