from django.db import models

from empleado.models import Empleado

#producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    precio = models.DecimalField(decimal_places=2, max_digits=100)
    cantidadDisponible = models.IntegerField()
    unidadMedida = models.CharField(max_length=50)
    tipo = models.CharField(max_length=200)
    imagen = models.FileField(default='default_image.jpg')

    def venta(self, cantidadVendida):
        if cantidadVendida <= self.cantidadDisponible:
            self.cantidadDisponible -= cantidadVendida
            self.save()
        else:
            raise ValueError("No hay suficientes unidades en Stock")

    def aumentoStock(self, cantidad):
        self.cantidadDisponible += cantidad
        self.save()

    def __str__(self):
        return self.nombre



#clientemayorista
class ClienteMayorista(models.Model):
    cuit = models.CharField(max_length=11, unique=True)
    nombreCompleto = models.CharField(max_length=250)
    domicilioCalle = models.CharField(max_length=200)
    domicilioNumero = models.IntegerField()
    domicilioLocalidad = models.CharField(max_length=200)
    domicilioDepartamento = models.CharField(max_length=200)


    def __str__(self):
        return self.nombreCompleto + " " + self.cuit

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
    # empleado
    empleadoVenta = models.ForeignKey(Empleado,on_delete=models.CASCADE,default=100)
    clienteM = models.ForeignKey(ClienteMayorista, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.numComprobante



#items
class Item(models.Model):
    prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subTotal = models.DecimalField(max_digits=100,decimal_places=2)

    def __str__(self):
        return f"{self.prod} - {self.cantidad} - {self.subtotal}"

