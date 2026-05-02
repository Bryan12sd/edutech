from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Estudiante, Matricula, Curso

@login_required
def perfil(request):
    estudiante = get_object_or_404(Estudiante, user=request.user)
    matriculas = Matricula.objects.filter(estudiante=estudiante)

    return render(request, 'perfil.html', {
        'estudiante': estudiante,
        'matriculas': matriculas
    })