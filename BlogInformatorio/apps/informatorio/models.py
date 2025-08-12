from django.db import models

# Create your models here.
#Modelo para los integrantes(página"integrantes") 
class Integrante(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	cargo = models.CharField(max_length=30)
	Biografia = models.TextField(blank=True)
	foto = models.ImageField(upload_to='integrantes', blank=True, null=True)
	email = models.EmailField(blank=True)
	orden = models.PositiveIntegerField(default=0, help_text='Orden de aparición')
	activo = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['orden', 'nombre']

	def __str__(self):
		return self.nombre

#Model para la sección "Donde estamos"
class Ubicacion(models.Model):
	nombre = models.CharField(max_length=150, default='Sede principal')
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=20)
	email = models.EmailField(blank=True)
	lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	mapa_embed = models.TextField(blank=True, help_text='Codigo iframe de google maps opcional')
	horario = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.nombre

#Modelo para_profes y para_estudiantes
class Persona(models.Model):
	CARGO_OPCIONES = [
		('estudiante', 'Estudiante'),
		('mentor', 'Mentor'),
		('profesor', 'Profesor'),
	]

	nombre = models.CharField(max_length=50)
	cargo = models.CharField(max_length=20, choices=CARGO_OPCIONES)
	Biografia = models.TextField()
	lugar_residencia = models.CharField(max_length=30)
	foto = models.ImageField(upload_to='profesor')
	proyectos = models.TextField(blank=True)
	activo = models.BooleanField(default=True)
	orden = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['orden', 'nombre']

	def __str__(self):
		return f'{self.nombre} ({self.get_cargo_display()})'
