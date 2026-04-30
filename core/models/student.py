from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

    def obtener_calificaciones(self):
        return self.calificacion_set.all()