from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from rest_framework.routers import DefaultRouter

from core.views import (
    login_view, dashboard, calificaciones, registro,
    horarios, crear_curso, matricula, perfil,
    EstudianteViewSet, CursoViewSet, CalificacionViewSet,
    HorarioViewSet, MatriculaViewSet, register_api, login_api,
)

# API ROUTER
router = DefaultRouter()
router.register('estudiantes', EstudianteViewSet)
router.register('cursos', CursoViewSet)
router.register('calificaciones', CalificacionViewSet)
router.register('horario', HorarioViewSet)
router.register('matriculas', MatriculaViewSet)

# URLS WEB + API
urlpatterns = [
    # AUTH
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),

    # WEB
    path('dashboard/', dashboard, name='dashboard'),
    path('calificaciones/', calificaciones, name='calificaciones'),
    path('registro/', registro, name='register'),
    path('horario/', horarios, name='horario'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('matricula/', matricula, name='matricula'),
    path('perfil/', perfil, name='perfil'),

    # API
    path('api/', include(router.urls)),
    path('api/register', register_api),
    path('api/login', login_api),
]
