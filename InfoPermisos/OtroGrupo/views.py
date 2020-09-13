from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


#from django.shortcuts import render

#from django.http import HttpResponse

#from appusuario.models import Usuario

#from appusuario.form import FormProducto

#from django.shortcuts import redirect

# Create your views here.

def home(request):
	return render(request, 'index.html', {})


def login(request):
	return render(request, 'login.html', {})


def perfil(request):
	return render(request, 'perfil.html', {})
