from django.shortcuts import render, redirect
from django.contrib.auth import logout as hacer_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as hacer_login
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required # Para filtrar por tipo de usuario: aprobador de permisos o solicitante.
from django.contrib.auth.models import User, Group

#Recursos de la misma app

from OtroGrupo.models import Ciudadano
from OtroGrupo.forms import CiudadanoForm



def home(request):
	return render(request, 'home.html', {})

# =========== View de Login ======================================================
def login(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			contrasenia = form.cleaned_data['password']
			user = authenticate(username=usuario, password=contrasenia)
			if user is not None:
				hacer_login(request, user)
				users_in_group = Group.objects.get(name="Permisor").user_set.all()
				if user in users_in_group:
					return redirect('permisor') # Si el usuario está en esa lista, te redirecciona a la vista permisor.
                # Y le redireccionamos al perfil de usuario.
				else:
					return redirect('perfil')
				hacer_login(request, user)
				return redirect('/')

	return render(request, "login.html", {'form':form})

#===================================================================================

def perfil(request):
	
	user = request.user
	if user.is_authenticated:
		return render(request, "perfil.html", {})
	else:
		return redirect("login")

	return render(request, "perfil.html", {})


def perfil_form(request):

	if request.user.is_authenticated:
		form = CiudadanoForm()
		if request.method == "POST":
			form = CiudadanoForm(request.POST)
			if form.is_valid():
				c_form = form.save(commit=False)
				c_form.user = request.user
				form.save()
				return redirect('detalles_guardados')
		else:
			form = CiudadanoForm()

		return render(request, "perfil_form.html", {'form':form})

	return redirect('login')
	
# ============== View de Registro ========================
def register(request):
	form = UserCreationForm()
	form.fields['username'].help_text = None
	form.fields['password1'].help_text = None
	form.fields['password2'].help_text = None
	if request.method == "POST":
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				hacer_login(request, user)
				return redirect('/')
	return render(request, "register.html", {'form':form})

# =========================================================
def logout(request):
	hacer_logout(request)

	return redirect('home')

# =========================================================

def detalles_guardados(request):

	return render(request, 'detalles_guardados.html', {})


def registro_exitoso(request):
	return render(request, 'register.html', {})


def solicitud(request):
	return render(request, 'solicitud.html', {})


def permisor_general(request):
	return render(request, 'permisor_general.html', {})


def permisor_revision(request):
	return render(request, 'permisor_revision.html', {})


def permisor_masDetalles(request):
	return render(request, 'permisor_masDetalles.html', {})

def historial(request):
	return render(request, 'historial.html', {})

def estado(request):
	return render(request, 'estado.html', {})