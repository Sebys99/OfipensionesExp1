from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('cronogramas/', views.cronograma_list, name='cronogramaList'),
    path('cronogramacreate/', csrf_exempt(views.crear_cronograma), name='cronogramaCreate'),
]