from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth
from . import views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='path_home'),


    #INCLUIR LAS APP
    path('Noticias/', include('noticias.urls')),
    path('Usuarios/', include('usuarios.urls')),
    path('Generos/', include('generos.urls')),
    path('Comentarios/', include('comentarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
