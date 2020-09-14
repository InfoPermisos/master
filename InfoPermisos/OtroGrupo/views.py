from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import UsuarioForm

#from django.shortcuts import render

#from django.http import HttpResponse

#from appusuario.models import Usuario

#from appusuario.form import FormProducto

#from django.shortcuts import redirect

# Create your views here.

def home(request):
	return render(request, 'index.html', {})


def login(request):
	my_form = UsuarioForm()
	if request.method == "POST":
		my_form = UsuarioForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
		"form": my_form,
	}

	return render(request, 'login.html', context)


def perfil(request):
	return render(request, 'perfil.html', {})
	

def register(request):
	return render(request, 'register.html', {})
