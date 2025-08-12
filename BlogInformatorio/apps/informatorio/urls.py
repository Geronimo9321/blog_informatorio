from django.urls import path
from . import views

app_name = "informatorio"

urlpatterns =[
	path('<slug:slug>/', views.mostrar_pagina, name='path_mostrar_pagina'),
]