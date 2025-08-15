from django.urls import path
from . import views

app_name = "noticias"

urlpatterns = [
    path('Listar', views.Listar_Noticias, name='path_listar_noticias'),
    path('Detalle/<int:pk>', views.DetalleNoticia.as_view(), name='path_detalle_noticias'),
    path('Crear/', views.CrearNoticia.as_view(), name='path_crear_noticias'),
    path('Modificar/<int:pk>', views.ModificarNoticia.as_view(), name='path_modificar_noticias'),
    path('Eliminar/<int:pk>', views.BorrarNoticia.as_view(), name='path_borrar_noticias'),
    path('buscar/', views.buscar_noticias, name='buscar_noticias'),

    #filtar noticias por generos
    path('Filtar/<int:pk>', views.Filtrar_Noticias, name='path_filtrar_noticias'),
]
