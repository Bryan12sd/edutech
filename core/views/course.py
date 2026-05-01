
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models.grade import Curso
from django.shortcuts import redirect

@login_required
def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Curso.objects.create(nombre=nombre)
        return redirect('dashboard')

    return render(request, 'curso.html')