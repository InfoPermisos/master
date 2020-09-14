from django import forms

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