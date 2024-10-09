from rest_framework import serializers
from . import models


class EstudianteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'cronograma', 'nombre', 'documento_identidad')
        model = models.Estudiante