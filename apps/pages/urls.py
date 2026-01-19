from django.urls import path
# Importamos las vistas
from .views import *

# Cargamos las URL para mostrar las vistas
urlpatterns = [
    path('', index, name="index"),
]
