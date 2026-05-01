from django.db import models
from django.contrib.auth.models import User
class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profesor')
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre