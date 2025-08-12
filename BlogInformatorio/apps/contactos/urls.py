from django.urls import path
from . import views

app_name = "noticias"

urlpatterns =[
	path('Contacto', views.contacto_view, name='path_contacto'),
]