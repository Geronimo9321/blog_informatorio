from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario
from noticias.models import Noticia
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseForbidden


# Create your views here.
def Comentar(request, pk):
    articulo = Noticia.objects.get(pk=pk)
    usuario = request.user
    comentario = request.POST.get('comentario', None)

    Comentario.objects.create(texto=comentario, noticia=articulo, usuario=usuario)

    return HttpResponseRedirect(reverse_lazy('noticias:path_detalle_noticias', kwargs={'pk': pk}))

class Eliminar(DeleteView):
    model = Comentario
    template_name = 'comentarios/comentario_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        comentario = self.get_object()
        user = request.user
        if not user.is_authenticated:
            return HttpResponseForbidden("No estás autenticado")
        
        if user.groups.filter(name='Colaborador').exists() or comentario.usuario == user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("No tenés permiso para borrar este comentario")

    def get_success_url(self):
        return reverse_lazy('noticias:path_detalle_noticias', kwargs={'pk': self.object.noticia.pk})