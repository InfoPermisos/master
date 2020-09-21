from django.shortcuts import render, redirect
from django.contrib.auth import logout as hacer_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as hacer_login
from .forms import UserFormExtras, MiAuthenticationForm 
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required # Para filtrar por tipo de usuario: aprobador de permisos o solicitante.
from django.contrib.auth.models import User, Group

#from django.shortcuts import render

#from django.http import HttpResponse

#from appusuario.models import Usuario

#from appusuario.form import FormProducto

#from django.shortcuts import redirect

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

# =========== View de Login ===========
def login(request):
    # Creamos el formulario de autenticación vacío
	form = MiAuthenticationForm()
	if request.method == "POST":
        # Añadimos los datos recibidos al formulario
		form = MiAuthenticationForm(data=request.POST)
        # Si el formulario es válido...
		if form.is_valid():
            # Recuperamos las credenciales validadas
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
			user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
			if user is not None:
                # Hacemos el login manualmente
				hacer_login(request, user)
				# Creamos una lista de usuarios que estén en el grupo 'Permisor'.
				users_in_group = Group.objects.get(name="Permisor").user_set.all()
				if user in users_in_group:
					return redirect('permisor') # Si el usuario está en esa lista, te redirecciona a la vista permisor.
                # Y le redireccionamos al perfil de usuario.
				else:
					return redirect('perfil')

    # Si llegamos al final renderizamos el formulario
	return render(request, "login.html", {'form': form})



def perfil(request):
	return render(request, 'perfil.html', {})
	
# ============== View de Registro ===================
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


def permisor_general(request):
	return render(request, 'permisor_general.html', {})


def permisor_revision(request):
	return render(request, 'permisor_revision.html', {})


def permisor_masDetalles(request):
	return render(request, 'permisor_masDetalles.html', {})