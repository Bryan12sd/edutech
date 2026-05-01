from django import forms
from django.contrib.auth.models import User

ROL_CHOICES = (
    ('estudiante', 'Estudiante'),
    ('profesor', 'Profesor'),
)

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")
    rol = forms.ChoiceField(choices=ROL_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('password2'):
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data