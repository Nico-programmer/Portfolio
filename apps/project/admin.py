from django.contrib import admin
# Obtenemos el modelo
from .models import Project

# Registramos el modelo en el admin
admin.site.register(Project)