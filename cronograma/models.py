from django.db import models

# Create your models here.

class Cronograma(models.Model):
    num_cuentas = models.IntegerField(default =None,null=True,blank=True)
    monto_total = models.FloatField(default=None,null=True,blank=True)
    periodo_total = models.IntegerField(default =None,null=True,blank=True)

    def __str__(self):
        return '%s %s %s' % (self.num_cuentas, self.monto_total, self.periodo_total)