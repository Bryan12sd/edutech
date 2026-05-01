from django.db import models
from .student import Estudiante
from .grade import Curso
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')

    def __str__(self):
        return f"{self.estudiante} - {self.curso}"