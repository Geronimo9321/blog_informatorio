from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Noticia
from .forms import FormularioCrearNoticia, FormularioModificarNoticia 
from .models import Genero

#DECORADOR PARA UNA VBF QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.decorators import login_required

#MIXINS PARA UNA VBC QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.mixins import LoginRequiredMixin

#Decorador para una VBF para controlar si el usuario es estaff
from django.contrib.admin.views.decorators import staff_member_required

#MIXIN PARAUNA VBC PARA CONTROLAR EL TIPO DE USUARIO (lo usamos para ver si es staff)
from django.contrib.auth.mixins import UserPassesTestMixin

#VISTA BASADA EN FUNCIONES
@login_required
@staff_member_required
def Listar_Noticias(request):
    valor_a_ordenar = request.GET.get('orden', None)

    #Ordenamiento
    if valor_a_ordenar:
        if valor_a_ordenar == 'asc':
            noticias = Noticia.objects.all().order_by('creado')
        elif valor_a_ordenar == 'desc':
            noticias = Noticia.objects.all().order_by('-creado')
        else:
            noticias = Noticia.objects.all()
    else:
        noticias = Noticia.objects.all()
    
    generos = Genero.objects.all()
    
    return render(request, 'Noticias/noticias.html',{'noticias': noticias, 'generos': generos})

def Filtrar_Noticias(request, pk):
    generos_filtrados = Genero.objects.get(pk = pk)
    noticias_filtradas = Noticia.objects.filter(Genero=generos_filtrados)
    return render(request, 'Noticias/filtrarNoticias.html', 
                  {'noticias': noticias_filtradas, 'genero': generos_filtrados})

class DetalleNoticia(DetailView):
    model = Noticia
    template_name = 'Noticias/detalleNoticias.html'
    context_object_name = 'noticias'

class CrearNoticia(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Noticia
    template_name = 'Noticias/crearNoticias.html'
    form_class = FormularioCrearNoticia
    success_url = reverse_lazy('noticias:path_listar_noticias')

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

class ModificarNoticia(UpdateView):
    model = Noticia
    template_name = 'Noticias/modificarNoticias.html'
    form_class = FormularioModificarNoticia
    success_url = reverse_lazy('noticias:path_listar_noticias')

class BorrarNoticia(DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:path_listar_noticias')