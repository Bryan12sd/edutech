from django.db import models
from django.contrib.auth.models import User
class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

    def obtener_calificaciones(self):
        return self.calificacion_set.all()