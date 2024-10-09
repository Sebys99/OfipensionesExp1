from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'cronograma',
            'nombre',
            'documento_identidad',
        ]

        labels = {
            'cronograma' : 'Cronograma',
            'nombre' : 'Nombre',
            'documento_identidad' : 'Documento_identidad',
        }