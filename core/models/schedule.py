from django.db import models
from .student import Estudiante
from .grade import Curso
class Horario(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.curso.nombre} - {self.dia} {self.hora}"