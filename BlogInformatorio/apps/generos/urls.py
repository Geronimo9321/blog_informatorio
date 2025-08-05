from django.urls import path
from . import views

app_name = 'generos'

urlpatterns = [
    path('Generos/', views.Listar_Generos, name='listar_generos'),
]