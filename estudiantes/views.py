from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import EstudianteForm
from .logic.estudiantes_logic import get_estudiantes,get_estudiantes_aldia,create_estudiante
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import EstudianteSerializer
import json

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
    