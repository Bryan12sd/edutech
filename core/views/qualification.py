from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.qualifications import Calificacion
from ..serializers import CalificacionSerializer
from rest_framework import viewsets
@login_required
def calificaciones(request):
    calificaciones = Calificacion.objects.select_related('estudiante', 'curso')
    return render(request, 'calificaciones.html', {'calificaciones': calificaciones})
class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer