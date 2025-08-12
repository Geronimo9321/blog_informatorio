from django.shortcuts import render, get_object_or_404
from .models import Pagina

# Create your views here.
def mostrar_pagina(request, slug):
	pagina = get_object_or_404(Pagina, slug=slug)
	return render(request, f'Informatorio/{slug}.html', {'contenido': pagina.contenido})