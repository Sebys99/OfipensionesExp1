from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import EstudianteForm
from .logic.estudiantes_logic import get_estudiantes,get_estudiantes_aldia,create_estudiante, get_estudiante
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import EstudianteSerializer
import json 
import datetime

def estudiante_list(request):
    estudiantes = get_estudiantes()
    serializer = EstudianteSerializer(estudiantes,many=True)
    context = {
        'estudiante_list': serializer.data
    }
    return JsonResponse(context)

def estudiante_list_al_dia(request):
    estudiantes = get_estudiantes_aldia()
    serializer = EstudianteSerializer(estudiantes,many=True)
    context = {
        'estudiante_list_al_dia': serializer.data
    }
    return JsonResponse(context)

def crear_estudiante(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = EstudianteForm(data)
        if form.is_valid():
            create_estudiante(form)
            return JsonResponse({"mensaje": "Estudiante creado exitosamente"}, status=201)
        else:
            print(form.errors)
            return JsonResponse({"mensaje": "No se pudo crear el estudiante"}, status=500)
    else:
        return JsonResponse({"mensaje": "No se pudo crear el estudiante"}, status=500)
    
def factura_estudiante(request, id_est):
    estudiante = get_estudiante(id_est)
    if estudiante:
        context = {
            'mensaje': 'Factura generada con éxito',
            'fecha_generacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'estudiante': {
                'nombre': estudiante.nombre,
                'documento': estudiante.documento_identidad,
                'cronograma': {
                    'valor': estudiante.cronograma.monto_total,
                    'periodo': estudiante.cronograma.periodo_total
                }
            }
        }
        return JsonResponse(context, status = 200)
    else:
        return JsonResponse({'mensaje':'Estudiante no encontrado'}, status = 404)
    