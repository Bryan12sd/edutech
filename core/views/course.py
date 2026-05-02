from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.grade import Curso
from django.shortcuts import redirect
from ..serializers import CursoSerializer
from rest_framework import viewsets
from django.contrib import messages


@login_required
def crear_curso(request):
    print("ENTRO A LA VISTA")
    if request.method == 'POST':
        # Crear el curso con todos los campos
        curso = Curso.objects.create(
            nombre=request.POST.get('nombre'),
            codigo=request.POST.get('codigo'),
            creditos=request.POST.get('creditos') or None,
            categoria=request.POST.get('categoria') or None,
            nivel=request.POST.get('nivel') or None,
            descripcion=request.POST.get('descripcion') or None,
            # profesor se asignaría desde un select con profesores
            duracion=request.POST.get('duracion') or None,
            cupo=request.POST.get('cupo') or None,
            color=request.POST.get('color', '#3b82f6'),
            activo=request.POST.get('activo') == 'on',
        )
        print(request.POST)
        messages.success(request, f'Curso "{curso.nombre}" creado exitosamente')
        return redirect('dashboard')  # o a donde quieras redirigir

    return render(request, 'curso.html')


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
