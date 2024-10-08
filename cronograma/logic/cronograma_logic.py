from django.http import JsonResponse
from ..models import Cronograma
import json
from django.core.serializers.json import DjangoJSONEncoder
from ..serializers import CronogramaSerializer

def get_cronogramas():
    queryset = Cronograma.objects.all()
    return (queryset)

def create_cronograma(form):
    cronograma = form.save()
    cronograma.save()
    return ()
