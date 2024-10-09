from django.db import models

# Create your models here.
from django.db import models
from cronograma.models import Cronograma

class Estudiante(models.Model):
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s' % (self.nombre, self.documento_identidad)