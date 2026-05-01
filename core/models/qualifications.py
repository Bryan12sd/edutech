from django.db import models
from .student import Estudiante
from .grade import  Curso
class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificaciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='calificaciones')
    nota = models.FloatField()

    def __str__(self):
        return f"{self.estudiante} - {self.curso} - {self.nota}"