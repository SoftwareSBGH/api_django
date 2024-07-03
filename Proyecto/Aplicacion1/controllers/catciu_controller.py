# En miaplicacion/views.py

from django.http import JsonResponse
from Aplicacion1.models import Catciu

def getCatciu(request):
    # Obtener todos los registros de Catciu
    registros = Catciu.objects.all()
    # Convertir los registros a una lista de diccionarios
    registros_list = list(registros.values())
    # Devolver la lista de registros como una respuesta JSON
    return JsonResponse(registros_list, safe=False)


