from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombreCompleto = models.CharField(max_length=250)
    telefono = models.CharField()
    email = models.EmailField()
    domicilioCalle = models.CharField(max_length=200)
    domicilioNumero = models.IntegerField()
    domicilioLocalidad = models.CharField(max_length=200)
    domicilioDepartamento = models.CharField(max_length=200)

    def darBaja(self):
        self.delete()

    def modificar(self, nombre, telefono, domicilioC, domicilioN, domicilioL, domicilioD):
        self.nombreCompleto = nombre
        self.telefono = telefono
        self.domicilioCalle = domicilioC
        self.domicilioNumero = domicilioN
        self.domicilioLocalidad = domicilioL
        self.domicilioDepartamento = domicilioD

        self.save()

    def __str__(self):
        return self.nombreCompleto