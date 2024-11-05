
# pedido/models.py
from django.db import models
from insumo.models import Insumo
from proveedor.models import Proveedor
from django.db.models import Sum



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
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=1)
    fecha_solicitud = models.DateField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Pedido {self.numero_pedido} - {self.proveedor.nombreCompleto}'


    # Método para calcular el total del pedido
    def total(self):
        return self.detalles.aggregate(total=Sum('precio_total'))['total'] or 0

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} de {self.insumo.nombre}'




##############RECEPCION PEDIDO#####################


#from django.contrib.auth.models import User
#from panaderia_mana.empleado.admin import Empleado
from empleado.models import Empleado


class RecepcionPedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='recepcion')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, default=1)
    fecha_recepcion = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Recepción de Pedido {self.pedido.numero_pedido}'
