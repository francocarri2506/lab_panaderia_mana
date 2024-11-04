from django.db import models

from apps.usuario.models import Usuario


# Create your models here.
class Empleado(models.Model):
    cuit = models.CharField(max_length=11, unique=True)
    nombreCompleto = models.CharField(max_length=250)
    telefono = models.CharField()
    fechaNacimiento = models.DateField()
    fechaIncorporacion = models.DateField()
    domicilioCalle = models.CharField(max_length=200)
    domicilioNumero = models.IntegerField()
    domicilioLocalidad = models.CharField(max_length=200)
    domicilioDepartamento = models.CharField(max_length=200)
    #usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombreCompleto + " " + self.cuit

