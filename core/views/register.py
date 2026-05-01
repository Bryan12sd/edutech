from ..forms import  RegistroForm
from django.shortcuts import redirect
from ..models import Estudiante
from django.shortcuts import render
from django.contrib.auth import login
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Crear estudiante automáticamente
            Estudiante.objects.create(
                user=user,
                nombre=user.username,
                email=user.email
            )
            login(request, user)

            return redirect('dashboard')

    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})