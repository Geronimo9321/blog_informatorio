from django.db import models
from generos.models import Genero

# Create your models here.
class Noticia(models.Model):
    creado = models.DateTimeField(
        auto_now_add = True
        )

    modificado = models.DateTimeField(
        auto_now = True
        )

    nombre = models.CharField(max_length= 30)
    
    imagen = models.ImageField(upload_to = 'noticias')
    
    genero = models.ForeignKey(Genero, null= True, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre 
    
    def misComentarios(self):
        return self.comentario_set.all()