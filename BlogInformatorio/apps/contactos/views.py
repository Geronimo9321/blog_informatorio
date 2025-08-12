from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def contacto_view(request):
	if request.method == 'post':
		form = ContactoForm(request.post)
		if form.is_valid():
			form.save()
	else:
		form = ContactoForm()

	return  render(request, 'Contactos/contacto.html', {'form': form})