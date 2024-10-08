from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import CronogramaForm
from .logic.cronograma_logic import get_cronogramas, create_cronograma
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import CronogramaSerializer

def cronograma_list(request):
    cronogramas = get_cronogramas()
    serializer = CronogramaSerializer(cronogramas,many=True)
    context = {
        'cronograma_list': serializer.data
    }
    return JsonResponse(context)

def crear_cronograma(request):
    if request.method == 'POST':
        print(request.POST)
        form = CronogramaForm(request.POST)
        print(form)
        if form.is_valid():
            create_cronograma(form)
            return JsonResponse({"mensaje": "Cronograma creado exitosamente"}, status=201)
        else:
            print(form.errors)
    else:
        return JsonResponse({"mensaje": "No se pudo crear el cronograma"}, status=500)
    
    