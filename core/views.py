from django.shortcuts import render
from .models import Estudiante ,Calificacion

def login_view(request):
    return render(request, 'login.html')


def dashboard(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'dashboard.html', {'estudiantes': estudiantes})

def calificaciones(request):
    calificaciones = Calificacion.objects.select_related('estudiante', 'curso')
    return render(request, 'calificaciones.html', {'calificaciones': calificaciones})