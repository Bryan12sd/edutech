from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import login_view, dashboard, calificaciones, registro, horarios, crear_curso, matricula
from django.urls import reverse_lazy

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('calificaciones/', calificaciones, name='calificaciones'),
    path('registro/', registro, name='register'),
    path('horario/', horarios, name='horario'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('matricula/', matricula, name='matricula'),

]
