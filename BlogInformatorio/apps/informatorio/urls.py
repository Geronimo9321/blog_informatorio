from django.urls import path
from . import views

app_name = "informatorio"

urlpatterns =[
	path('Nuestra_institucion/', views.nuestra_institucion, name='path_nuestra_institucion'),
	path('Donde_estamos/', views.donde_estamos, name='path_donde_estamos'),
	path('Integrantes/', views.integrantes, name='path_integrantes'),
	path('Para_profes/', views.para_profes, name='path_para_profes'),
	path('Para_estudiants/', views.para_estudiantes, name='path_para_estudiantes'),
]