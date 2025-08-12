from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Noticia, Genero

from .forms import FormularioCrearNoticia, FormularioModificarNoticia

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import Group


@login_required
@staff_member_required
def Listar_Noticias(request):
    valor_a_ordenar = request.GET.get('orden', None)

    if valor_a_ordenar == 'asc':
        noticias = Noticia.objects.all().order_by('creado')
    elif valor_a_ordenar == 'desc':
        noticias = Noticia.objects.all().order_by('-creado')
    else:
        noticias = Noticia.objects.all()

    generos = Genero.objects.all()

    return render(request, 'Noticias/noticias.html', {'noticias': noticias, 'generos': generos})


def Filtrar_Noticias(request, pk):
    genero_filtrado = Genero.objects.get(pk=pk)
    noticias_filtradas = Noticia.objects.filter(genero=genero_filtrado)
    return render(request, 'Noticias/filtrarNoticias.html',
                  {'noticias': noticias_filtradas, 'genero': genero_filtrado})


class DetalleNoticia(DetailView):
    model = Noticia
    template_name = 'Noticias/detalleNoticias.html'
    context_object_name = 'noticia'


class ColaboradorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # Retorna True si el usuario está en el grupo 'Colaborador'
        return self.request.user.groups.filter(name='Colaborador').exists()

    def handle_no_permission(self):
        # Opcional: redirigir o mostrar error personalizado
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("No tienes permiso para realizar esta acción.")


class CrearNoticia(LoginRequiredMixin, ColaboradorRequiredMixin, CreateView):
    model = Noticia
    template_name = 'Noticias/crearNoticias.html'
    form_class = FormularioCrearNoticia
    success_url = reverse_lazy('noticias:path_listar_noticias')


class ModificarNoticia(LoginRequiredMixin, ColaboradorRequiredMixin, UpdateView):
    model = Noticia
    template_name = 'Noticias/modificarNoticias.html'
    form_class = FormularioModificarNoticia
    success_url = reverse_lazy('noticias:path_listar_noticias')


class BorrarNoticia(LoginRequiredMixin, ColaboradorRequiredMixin, DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:path_listar_noticias')
