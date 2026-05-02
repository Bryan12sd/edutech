from django.db import models
from .teacher import Profesor


class Curso(models.Model):
    # Campos básicos
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True)
    creditos = models.IntegerField(null=True, blank=True, verbose_name="Créditos")

    # Categorización
    CATEGORIAS = [
        ('matematicas', 'Matemáticas'),
        ('ciencias', 'Ciencias'),
        ('humanidades', 'Humanidades'),
        ('tecnologia', 'Tecnología'),
        ('idiomas', 'Idiomas'),
        ('artes', 'Artes'),
        ('deportes', 'Deportes'),
    ]
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, null=True, blank=True)

    NIVELES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    nivel = models.CharField(max_length=15, choices=NIVELES, null=True, blank=True)

    # Detalles
    descripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripción")
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True, related_name='cursos')

    DURACIONES = [
        ('bimestral', 'Bimestral (2 meses)'),
        ('trimestral', 'Trimestral (3 meses)'),
        ('semestral', 'Semestral (6 meses)'),
        ('anual', 'Anual (12 meses)'),
    ]
    duracion = models.CharField(max_length=15, choices=DURACIONES, null=True, blank=True)

    # Configuración
    cupo = models.IntegerField(null=True, blank=True, verbose_name="Cupo Máximo")
    color = models.CharField(max_length=7, default='#3b82f6', verbose_name="Color Identificador")  # Formato hexadecimal
    icono = models.CharField(max_length=50, default='book', verbose_name="Icono FontAwesome")  # Sin 'fas fa-'
    activo = models.BooleanField(default=True, verbose_name="Curso Activo")

    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    @property
    def estudiantes_count(self):
        """Retorna el número de estudiantes matriculados"""
        return self.matriculas.count()