from django.urls import path
from . import views

app_name = "noticias"

urlpatterns = [
    path('Listar', views.Listar_Noticias, name='path_listar_noticias'),
]
