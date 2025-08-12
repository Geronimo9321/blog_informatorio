from django.db import models

# Create your models here.
class Pagina(models.Model):
	titulo = models.CharField(max_length=100) #Título visible para el admin y representación
	slug = models.SlugField(unique=True) #Slug para URL amigable, único para cada página (ej: "nuestra_institucion")
	contenido = models.TextField() #Contenido editable que se mostrará en la página
	fecha_creacion = models.DateTimeField(auto_now_add=True) #Fecha de creación automática, solo lectura

	def __str__(self):
		return self.titulo