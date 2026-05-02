from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from core.forms import RegistroForm
from core.models import Estudiante, Profesor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..models  import Estudiante
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            rol = form.cleaned_data['rol']

            user = User.objects.create_user(
                username=form.cleaned_data['email'],  # login con email
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            if rol == 'estudiante':
                Estudiante.objects.create(
                    user=user,
                    nombre=form.cleaned_data['username']
                )

            elif rol == 'profesor':
                Profesor.objects.create(
                    user=user,
                    nombre=form.cleaned_data['username']
                )

            login(request, user)
            return redirect('dashboard')

    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})



@api_view(['POST'])
def register_api(request):
    username = request.data.get('username')  # nombre real
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({"error": "Todos los campos son obligatorios"}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email ya registrado"}, status=400)

    user = User.objects.create_user(
        username=email,  # login con email
        email=email,
        password=password
    )

    Estudiante.objects.create(
        user=user,
        nombre=username
    )

    return Response({"message": "Usuario registrado"}, status=201)