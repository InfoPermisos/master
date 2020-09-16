from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.Form):
	email = forms.EmailField(
		label='',
		widget= forms.EmailInput(
			attrs={
				"placeholder":"Ingrese su email",
				"required":"True",
				"style":
				 	"width:100%;" +
				 	"border-radius: 200px 200px 200px 200px;-moz-border-radius: 200px 200px 200px 200px;-webkit-border-radius: 200px 200px 200px 200px;border: 0px solid #000000;" +
				 	"font-size: 1em;" +
				 	"height: 1em;" +
				 	"padding: 0.5em;" +
				 	"text-align:center;" +
				 	"margin-bottom: 3%;" +
				 	"margin-top: 3%;"
				}
			)
		)
	clave = forms.CharField(
		label='',
		widget= forms.TextInput(

			attrs={
				"type":"password",
				"placeholder":"Ingrese su clave",
				 "style":
				 	"width:100%;" +
				 	"border-radius: 200px 200px 200px 200px;-moz-border-radius: 200px 200px 200px 200px;-webkit-border-radius: 200px 200px 200px 200px;border: 0px solid #000000;" +
				 	"font-size: 1em;" +
				 	"height: 1em;" +
				 	"padding: 0.5em;" +
				 	"text-align:center;" +
				 	"margin-bottom: 3%;"
				}
			)
		)

# ================================REGISTRO=================================================

class UserFormExtras(UserCreationForm):
	#Utilizo este dic general para aplicar en cada campo los estilos generales de CSS.
	dic_style = {
	"style":
		"width:100%;" +
		"border-radius: 200px 200px 200px 200px;-moz-border-radius: 200px 200px 200px 200px;-webkit-border-radius: 200px 200px 200px 200px;border: 0px solid #000000;" +
		"font-size: 1em;" +
		"height: 2em;" +
		"padding: 0.5em;" +
		"text-align:center;" +
		"margin-bottom: 3%;"
	}

	username = forms.EmailField(label="Email", widget=forms.TextInput(attrs=dic_style))
	password1 = forms.CharField(label="Contraseña", help_text=None, widget=forms.TextInput(attrs=dic_style))
	password2 = forms.CharField(label="Re ingrese contraseña", help_text=None, widget=forms.TextInput(attrs=dic_style))
	nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs=dic_style))
	apellido = forms.CharField(label="Apellido", widget=forms.TextInput(attrs=dic_style))
	genero = forms.CharField(label="Género", widget=forms.TextInput(attrs=dic_style))
	dni = forms.IntegerField(label="DNI", widget=forms.TextInput(attrs=dic_style))
	fecha_nac = forms.DateField(label="Fecha de nacimiento", widget=forms.SelectDateWidget)

	class Meta:
		model = User
		fields = ["username", "password1", "password2", "nombre", "apellido", "genero", "dni", "fecha_nac"]