from rest_framework import serializers
from . import models

class CronogramaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'num_cuentas', 'monto_total', 'periodo_total')
        model = models.Cronograma