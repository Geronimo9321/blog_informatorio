from django import forms
from .models import Noticia

class FormularioCrearNoticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('nombre', 'imagen', 'genero')

class FormularioModificarNoticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('nombre', 'imagen', 'genero')