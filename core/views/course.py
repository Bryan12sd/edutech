
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.grade import Curso
from django.shortcuts import redirect
from ..serializers import CursoSerializer
from rest_framework import viewsets
@login_required
def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Curso.objects.create(nombre=nombre)
        return redirect('dashboard')

    return render(request, 'curso.html')
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer