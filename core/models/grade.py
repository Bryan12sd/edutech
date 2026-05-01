from django.db import models
from .teacher import Profesor

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre