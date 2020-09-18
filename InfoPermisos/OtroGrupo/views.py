from django.shortcuts import render, redirect
from django.contrib.auth import logout as hacer_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth import login as hacer_login
from .forms import UserFormExtras, UsuarioForm
from django.http import HttpResponse
from django.template import loader

#from django.shortcuts import render

#from django.http import HttpResponse

#from appusuario.models import Usuario

#from appusuario.form import FormProducto

#from django.shortcuts import redirect

# Create your views here.

def home(request):
	return render(request, 'home.html', {})


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
	form = UserFormExtras()
	form.fields['username'].help_text = None
	form.fields['password1'].help_text = None
	form.fields['password2'].help_text = None
	if request.method == "POST":
		form = UserFormExtras(data=request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				#hacer_login(request, user)
				return redirect('login')
	return render(request, "register.html", {'form':form})

def registro_exitoso(request):
	return render(request, 'register.html', {})

def solicitud(request):
	return render(request, 'solicitud.html', {})
