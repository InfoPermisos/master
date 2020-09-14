from django.db import models

# Create your models here.


class Usuario(models.Model):

	dni = models.IntegerField(primary_key = True)
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 254)
	clave = models.CharField(max_length = 100)