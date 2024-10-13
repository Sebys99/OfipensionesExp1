from ..models import Estudiante
from  django.core.exceptions import ObjectDoesNotExist

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

def get_estudiantes_aldia():
    queryset = Estudiante.objects.filter(cronograma__monto_total=0)
    return (queryset)

def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()

def get_estudiante(id_est: int):
    try:
        estudiante = Estudiante.objects.get(documento_identidad=id_est)
        return (estudiante)
    except ObjectDoesNotExist:
        return None