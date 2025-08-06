from django.shortcuts import render
from generos.models import Genero

# Create your views here.

def Listar_Generos(request):
    generos = Genero.objects.all()
    return render(request, 'Generos/generos.html',{'generos':generos})