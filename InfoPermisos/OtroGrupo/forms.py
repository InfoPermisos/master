from django import forms
from django.forms import ModelForm
from OtroGrupo.models import Ciudadano, Administrador, Permiso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.Form):
	email = forms.EmailField(
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
	clave = forms.CharField(
		label='',
		widget= forms.TextInput(

			attrs={
				"class":"input-form",
				"type":"password",
				"placeholder":"Ingrese su clave",
				}
			)
		)

# ================================REGISTRO=================================================

class UserFormExtras(UserCreationForm):
	username = forms.EmailField(label="Email")
	nombre = forms.CharField(label="Nombre")
	apellido = forms.CharField(label="Apellido")
	genero = forms.CharField(label="Género")
	dni = forms.IntegerField(label="DNI")
	fecha_nac = forms.DateField(label="Fecha de nacimiento", widget=forms.SelectDateWidget(years=range(1900, 2100)))

	class Meta:
		model = User
		fields = ["username", "password1", "password2", "nombre", "apellido", "genero", "dni", "fecha_nac"]

class CiudadanoForm(ModelForm):
	class Meta:
		model = Ciudadano
		fields = ['id', 'dniId', 'fechaNacimiento', 'ciudad', 'empleo', 'enfermedades', 'isopado', 'fechaIsopado']


class AdministradorForm(ModelForm):
	class Meta:
		model = Administrador
		fields = ['id', 'dniId']


class PermisoForm(ModelForm):
	class Meta:
		model = Permiso
		fields = ['id', 'ciudadanoId', 'administradorId', 'tipoPermiso', 'estado', 'detalle', 'motivo']

