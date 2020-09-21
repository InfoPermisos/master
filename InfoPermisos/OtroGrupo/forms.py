from django import forms
from django.forms import ModelForm
from OtroGrupo.models import Ciudadano, Administrador, Permiso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# =========================LOGIN======================================================

class MiAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
		label='',
		widget= forms.EmailInput(
			attrs={
				"class":"input-form",
				"type":"email",
				"placeholder":"Ingrese su email",
				"required":"True",
				}
			)
		)
    
    password = forms.CharField(
    	label='',
    	widget=forms.PasswordInput(
    		attrs={
				"class":"input-form",
				"type":"password",
				"placeholder":"Ingrese su clave",
			}
    	)
    )
# ================================REGISTRO=================================================

class UserFormExtras(UserCreationForm):
	# Lista de tuplas, donde cada tupla representa un "choice".
	genero_choices = [
		('Masculino', 'Masculino'),
		('Femenino', 'Femenino'),
		('Otro', 'Otro')
	]
	username = forms.EmailField(label="Email")
	nombre = forms.CharField(label="Nombre")
	apellido = forms.CharField(label="Apellido")
	genero = forms.ChoiceField(label="Género", choices=genero_choices)
	dni = forms.IntegerField(label="DNI")
	fecha_nac = forms.DateField(label="Fecha de nacimiento", widget=forms.SelectDateWidget(years=range(1900, 2100)))

	class Meta:
		model = User
		fields = ["username", "password1", "password2", "nombre", "apellido", "genero", "dni", "fecha_nac"]


class CiudadanoForm(ModelForm):
	class Meta:
		model = Ciudadano
		fields = ['id', 'dniId', 'fechaNacimiento', 'ciudad', 'empleo', 'enfermedades', 'isopado', 'fechaIsopado']
		widgets = {

		}


class AdministradorForm(ModelForm):
	class Meta:
		model = Administrador
		fields = ['id', 'dniId']
		widgets = {

		}



class PermisoForm(ModelForm):
	class Meta:
		model = Permiso
		fields = ['id', 'ciudadanoId', 'administradorId', 'tipoPermiso', 'estado', 'detalle', 'motivo']
		widgets = {

		}

