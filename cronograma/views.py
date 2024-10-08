from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CronogramaForm
from .logic.cronograma_logic import get_cronogramas, create_cronograma, get_cronograma
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def cronograma_list(request):
    cronogramas = get_cronogramas()
    context = {
        'cronograma_list': cronogramas
    }
    return JsonResponse(context)

@csrf_exempt
def crear_cronograma(request):
    if request.method == 'POST':
        data = request.POST 
        form = CronogramaForm(data)
        return create_cronograma(form)
    
@csrf_exempt
def cronograma(request):
    if request.method == 'GET':
        data = request.GET 
        cronograma = get_cronograma(data)
        return JsonResponse(cronograma)
    