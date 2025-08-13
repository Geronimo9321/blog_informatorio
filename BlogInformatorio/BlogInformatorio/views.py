from django.shortcuts import render
from noticias.models import Noticia, Genero  # Asegurate que tu app se llame "noticias"

def Home(request):
    # Traer parámetros GET
    orden = request.GET.get('orden', 'desc')  # default: descendente
    etapa = request.GET.get('etapa', '')      # default: todas

    # Filtrar por etapa si se selecciona
    noticias = Noticia.objects.all()
    if etapa:
        noticias = noticias.filter(genero__pk=etapa)

    # Ordenar por fecha
    if orden == 'asc':
        noticias = noticias.order_by('creado')
    else:
        noticias = noticias.order_by('-creado')

    # Traer todas las etapas (generos)
    generos = Genero.objects.all()

    context = {
        'noticias': noticias,
        'generos': generos,
        'orden': orden,
        'etapa': etapa,
    }

    return render(request, 'home.html', context)
