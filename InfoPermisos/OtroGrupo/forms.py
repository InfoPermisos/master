from django import forms

class UsuarioForm(forms.Form):
	email = forms.EmailField(
		label='',
		widget= forms.EmailInput(
			attrs={
				"placeholder":"Ingrese su email",
				"required":"True",
				"class":"formulario",
				}
			)
		)
	clave = forms.CharField(
		label='',
		widget= forms.TextInput(

			attrs={
				"type":"password",
				"placeholder":"Ingrese su clave",
				"class":"formulario",
				}
			)
		)