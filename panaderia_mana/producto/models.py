from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    precio = models.DecimalField(decimal_places=2, max_digits=100)
    cantidadDisponible = models.IntegerField()
    unidadMedida = models.CharField(max_length=50)
    tipo = models.CharField(max_length=200)

    def venta(self, cantidadVendida):
        if cantidadVendida <= self.cantidadDisponible:
            self.cantidadDisponible -= cantidadVendida
            self.save()
        else:
            raise ValueError("No hay suficientes unidades en Stock")

    def aumentoStock(self, cantidad):
        self.cantidadDisponible += cantidad
        self.save()

    def darBaja(self):
        self.delete()

    def modificar(self, nombre, descripcion, precio, unidadMedida, tipo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.unidadMedida = unidadMedida
        self.tipo = tipo

        self.save()

    def __str__(self):
        return self.nombre