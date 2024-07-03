# En Aplicacion1/urls.py (crea este archivo si no existe)
from django.urls import path
from Aplicacion1.controllers import catciu_controller

urlpatterns = [
    path('getCatciu/', catciu_controller.getCatciu, name='getCatciu'),
    # Define la URL para mi_vista. El nombre 'mi_vista' es opcional pero útil para referencias inversas.
    # La ruta 'mi_vista/' indica que la vista se mostrará en http://127.0.0.1:8000/mi_vista/ o http://localhost:8000/mi_vista/
]
