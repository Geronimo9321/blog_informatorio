from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuarios

# Create your views here.
class RegistroUsuarios(CreateView):
    template_name = 'Usuarios/registro.html'
    form_class = FormularioRegistroUsuarios
    success_url = reverse_lazy('usuarios:path_login')