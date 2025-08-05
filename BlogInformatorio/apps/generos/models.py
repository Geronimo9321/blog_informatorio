from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='generos', null=True)

    def __str__(self):
        return self.nombre