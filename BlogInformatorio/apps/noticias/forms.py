from django import forms
from .models import Noticia

class FormularioCrearNoticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('nombre', 'imagen', 'genero', 'descripcion')

class FormularioModificarNoticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('nombre', 'imagen', 'genero', 'descripcion')