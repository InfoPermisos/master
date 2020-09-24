from django import forms
from django.forms import ModelForm
from OtroGrupo.models import Ciudadano

# Este form se inserta en perfil_form.html

class CiudadanoForm(forms.ModelForm):
	
	class Meta:
		model = Ciudadano
		fields = (
			'email', 'first_name', 'last_name', 'dni',
			'fecha_nacimiento', 'genero', 'ciudad', 'empleo',
			'enfermedades', 'isopado', 'fecha_isopado'
		)