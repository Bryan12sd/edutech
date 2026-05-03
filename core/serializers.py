from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# 1. ESTUDIANTE
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


# 2. CURSO
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


# 3. CALIFICACION
class CalificacionSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.CharField(source='estudiante.nombre', read_only=True)
    curso_nombre = serializers.CharField(source='curso.nombre', read_only=True)

    class Meta:
        model = Calificacion
        fields = ['id', 'nota', 'estudiante', 'curso', 'estudiante_nombre', 'curso_nombre']


# 4. HORARIO
class HorarioSerializer(serializers.ModelSerializer):
    curso_nombre = serializers.CharField(source='curso.nombre', read_only=True)
    estudiante_nombre = serializers.CharField(source='estudiante.nombre', read_only=True)

    class Meta:
        model = Horario
        fields = ['id', 'dia', 'hora', 'curso', 'estudiante', 'curso_nombre', 'estudiante_nombre']


# 5. MATRICULA
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
