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
