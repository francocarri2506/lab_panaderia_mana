from django.db import models

# Create your models here.
class Venta(models.Model):
    tipoCliente = models.CharField(max_length=100)
    fechaVenta = models.DateField()
    tipoVenta = models.CharField(max_length=100)
    formaPago = models.CharField(max_length=100)
    tipoComprobante = models.CharField(max_length=100)
    numComprobante = models.IntegerField(unique=True)
    montoTotal = models.DecimalField(decimal_places=2, max_digits=100)
    observaciones = models.CharField(max_length=1000)

    #producto
    #empleado
    #clientemayorista

    #items

    def __str__(self):
        return self.numComprobante