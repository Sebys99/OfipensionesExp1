from ..models import Cronograma

def get_cronogramas():
    queryset = Cronograma.objects.all()
    return (queryset)

def create_cronograma(form):
    cronograma = form.save()
    cronograma.save()
    return ()

def get_cronograma(id):
    try:
        cronograma = Cronograma.objects.get(id=id)
        return {'existe': True, 'id': cronograma.id}
    except Cronograma.DoesNotExist:
        return None