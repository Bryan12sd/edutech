from django.contrib import admin
from .models import Estudiante, Curso, Calificacion,Horario, Matricula

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Calificacion)
admin.site.register(Horario)
admin.site.register(Matricula)