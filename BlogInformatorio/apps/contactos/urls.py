from django.urls import path
from . import views

app_name = "contactos"

urlpatterns =[
	path('Contacto', views.contacto_view, name='path_contactos'),
]