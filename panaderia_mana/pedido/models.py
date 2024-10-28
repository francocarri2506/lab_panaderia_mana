#from django.db import models

# Create your models here.
#class Pedido(models.Model):
    #numeroPedido = models.IntegerField(unique=True)
#    fechaEmision = models.DateField()
#fechaRecepcion = models.DateField()
#    observacionesPeticion = models.CharField(max_length=1000)
#   montoTotal = models.DecimalField(max_digits=100,decimal_places=2)
#   numeroComprobante = models.IntegerField()
#   observacionesLlegada = models.CharField(max_length=1000)

#    def __str__(self):
#       return self.numeroPedido

# pedido/models.py
from django.db import models
from insumo.models import Insumo
from proveedor.models import Proveedor

"""
class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='pedidos')
    fecha_emision = models.DateTimeField(auto_now_add=True)
    fechaRecepcion = models.DateField()
    numero_pedido = models.IntegerField()
    
    monto_total = models.FloatField(default=0.0)

    def __str__(self):
        return f"Pedido {self.numero_pedido} - {self.proveedor.nombre}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f"{self.insumo.nombre} - {self.cantidad} unidades"

"""

"""
class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
"""

class Pedido(models.Model):
    numero_pedido = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=1)
    fecha_solicitud = models.DateField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Pedido {self.numero_pedido} - {self.proveedor.nombreCompleto}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} de {self.insumo.nombre}'