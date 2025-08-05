from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuario

# Create your views here.
class RegistroUsuarios(CreateView):
    template_name = 'Usuarios/registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('usuarios:path_login')