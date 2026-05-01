from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='estudiante')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre