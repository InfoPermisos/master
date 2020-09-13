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
	#lista = Usuario.objects.all()
	

	return ("estas en el home")

def login(request):

	return ("estas en el login")

def perfil(request):

	return ("estas en el perfil")