from django.db import models
from .student import Estudiante
from .grade import  Curso
class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"{self.estudiante} - {self.curso} - {self.nota}"