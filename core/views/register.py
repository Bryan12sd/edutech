from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from core.forms import RegistroForm
from core.models import Estudiante, Profesor

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