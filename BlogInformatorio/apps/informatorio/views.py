from django.shortcuts import render

# Create your views here.
def nuestra_institucion(request):
	return render(request, 'Informatorio/nuestra_institucion.html')

def donde_estamos(request):
	return render(request, 'Informatorio/donde_estamos.html')

def integrantes(request):
	return render(request, 'Informatorio/integrantes.html')

def para_profes(request):
	return render(request, 'Informatorio/para_profes.html')

def para_estudiantes(request):
	return render(request, 'Informatorio/para_estudiantes.html')