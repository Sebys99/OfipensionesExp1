from django import forms
from .models import Cronograma

class CronogramaForm(forms.ModelForm):
    class Meta:
        model = Cronograma
        fields = [
            'num_cuentas',
            'monto_total',
            'periodo_total'
        ]

        labels = {
            'num_cuentas' : 'Num_cuentas',
            'monto_total' : 'Monto_total',
            'periodo_total' : 'Periodo_total'
        }