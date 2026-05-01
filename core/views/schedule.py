from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models.schedule import Horario
from ..models.student import Estudiante
@login_required
def horarios(request):
    estudiante = get_object_or_404(Estudiante, user=request.user)
    horarios = Horario.objects.filter(estudiante=estudiante)

    return render(request, 'horario.html', {
        'horarios': horarios
    })