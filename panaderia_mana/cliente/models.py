from django.db import models

# Create your models here.
class ClienteMayorista(models.Model):
    cuit = models.CharField(max_length=11, unique=True)
    nombreCompleto = models.CharField(max_length=250)
    domicilioCalle = models.CharField(max_length=200)
    domicilioNumero = models.IntegerField()
    domicilioLocalidad = models.CharField(max_length=200)
    domicilioDepartamento = models.CharField(max_length=200)

    def darBaja(self):
        self.delete()

    def modificar(self, cuit, nombre, domicilioC, domicilioN, domicilioL, domicilioD):
        self.cuit = cuit
        self.nombreCompleto = nombre
        self.domicilioCalle = domicilioC
        self.domicilioNumero = domicilioN
        self.domicilioLocalidad = domicilioL
        self.domicilioDepartamento = domicilioD

        self.save()

    def __str__(self):
        return self.nombreCompleto + " " + self.cuit