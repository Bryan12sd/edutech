from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Estudiante, Matricula, Curso


@login_required
def matricula(request):
    estudiante = get_object_or_404(Estudiante, user=request.user)

    cursos = Curso.objects.all()
    matriculas = Matricula.objects.filter(estudiante=estudiante)

    if request.method == 'POST':
        curso_id = request.POST.get('curso')
        curso = Curso.objects.get(id=curso_id)

        # evitar duplicados
        existe = Matricula.objects.filter(estudiante=estudiante, curso=curso).exists()

        if not existe:
            Matricula.objects.create(estudiante=estudiante, curso=curso)

    return render(request, 'matricula.html', {
        'cursos': cursos,
        'matriculas': matriculas
    })
