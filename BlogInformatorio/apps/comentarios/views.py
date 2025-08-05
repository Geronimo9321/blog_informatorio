from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario
from noticias.models import Noticia
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
def Comentar(request,pk):
    articulo = Noticia.objects.get(pk = pk)
    usuario = request.user
    comentario = request.POST.get('comentario',None)

    Comentario.objects.create(texto = comentario, Noticia = articulo, usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('noticias:path_detalle_noticias', kwargs={'pk':pk}))

class Eliminar(DeleteView):
    model = Comentario
    def get_success_url(self):
        return reverse_lazy('noticias:path_detalle_noticias', kwargs={'pk':self.object.noticia.pk})