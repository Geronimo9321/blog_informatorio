from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.db.models import Q

from .models import Noticia, Genero
from .forms import FormularioCrearNoticia, FormularioModificarNoticia


@method_decorator([staff_member_required], name='dispatch')
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
    
    es_colaborador = False
    if request.user.is_authenticated:
        es_colaborador = request.user.groups.filter(name='Colaborador').exists()
    
    return render(request, 'Noticias/filtrarNoticias.html', {
        'noticias': noticias_filtradas,
        'genero': genero_filtrado,
        'es_colaborador': es_colaborador
    })


def buscar_noticias(request):
    query = request.GET.get('q', '').strip()  # texto que escribe el usuario

    resultados = Noticia.objects.filter(
        Q(nombre__icontains=query) | Q(genero__nombre__icontains=query)
    ).distinct()

    return render(request, 'noticias/buscar.html', {
        'resultados': resultados,
        'query': query
    })

class DetalleNoticia(DetailView):
    model = Noticia
    template_name = 'Noticias/detalleNoticias.html'
    context_object_name = 'noticia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_colaborador'] = self.request.user.groups.filter(name='Colaborador').exists()
        return context


class ColaboradorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Colaborador').exists()

    def handle_no_permission(self):
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
