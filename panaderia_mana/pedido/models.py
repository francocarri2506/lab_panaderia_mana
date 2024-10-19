from django.db import models

# Create your models here.
class Pedido(models.Model):
    #numeroPedido = models.IntegerField(unique=True)
    fechaEmision = models.DateField()
    fechaRecepcion = models.DateField()
    observacionesPeticion = models.CharField(max_length=1000)
    montoTotal = models.DecimalField(max_digits=100,decimal_places=2)
    numeroComprobante = models.IntegerField()
    observacionesLlegada = models.CharField(max_length=1000)

    def __str__(self):
        return self.numeroPedido


class Pedido(models.Model):
    fecha_emision = models.DateTimeField()
    numero_pedido = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    monto_total = models.FloatField()

    def __str__(self):
        return f'Pedido #{self.numero_pedido}'