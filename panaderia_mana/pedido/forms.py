"""
from django import forms
from .models import Pedido, ItemPedido
from insumo.models import Insumo
from proveedor.models import Proveedor

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['proveedor', 'observaciones']

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['insumo', 'cantidad', 'precio']

    def __init__(self, *args, **kwargs):
        proveedor = kwargs.pop('proveedor', None)
        super().__init__(*args, **kwargs)
        if proveedor:
            self.fields['insumo'].queryset = Insumo.objects.filter(proveedores=proveedor)


"""

from django import forms
from django.forms import inlineformset_factory

from .models import Pedido, DetallePedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [ 'proveedor', 'fecha_solicitud', 'observaciones']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_solicitud': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control bg-faded', 'rows': 3, 'aria-describedby': 'basic-addon2'}),
        }

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['insumo', 'cantidad']
        widgets = {
            'insumo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control','min': '1'}),
        }

from django import forms
from .models import Pedido, DetallePedido
from django.forms import modelformset_factory
"""
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha']
"""
# Formulario para los detalles del pedido
DetallePedidoFormSet = modelformset_factory(DetallePedido, fields=('insumo', 'cantidad'), extra=0)


from django import forms
from .models import RecepcionPedido

class RecepcionPedidoForm(forms.ModelForm):
    class Meta:
        model = RecepcionPedido
        fields = ['observaciones']
        widgets = {
            'observaciones': forms.Textarea(
                attrs={'class': 'form-control bg-faded', 'rows': 3, 'aria-describedby': 'basic-addon2'}),
        }