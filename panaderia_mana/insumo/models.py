"""
from django.db import models

class Insumo(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_disponible = models.IntegerField()
    cantidad_minima = models.IntegerField()

    def aumentar_stock(self, cantidad):
        self.cantidad_disponible += cantidad
        self.save()

    def decrementar_stock(self, cantidad):
        if cantidad <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad
            self.save()
        else:
            raise ValueError("Cantidad a decrementar excede la cantidad disponible")

    def __str__(self):
        return self.nombre

"""


from django.db import models
#from proveedor.models import Proveedor

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_disponible = models.IntegerField()
    cantidad_minima = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=20000)
#    proveedores = models.ManyToManyField(Proveedor, related_name='insumos')

    def aumentar_stock(self, cantidad):
        self.cantidad_disponible += cantidad
        self.save()

    def decrementar_stock(self, cantidad):
        self.cantidad_disponible -= cantidad
        self.save()

    def __str__(self):
        return self.nombre