from django.db import models
from django.contrib.auth.models import User

class Ciudadano(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField('Email', blank=True, null = False)
    first_name = models.CharField('Nombre', max_length=100, blank = True, null = True)
    last_name = models.CharField('Apellido', max_length=100, blank = True, null = True)
    dni = models.IntegerField('DNI', primary_key=True, null = False)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento', blank = True, null = True)
    genero = models.CharField('Género', max_length = 20, null = True)
    ciudad = models.CharField('Ciudad',max_length = 126, null = True)
    empleo = models.CharField('Empleo',max_length = 126, null = True)
    enfermedades = models.CharField('Enfermedades',max_length = 126, null = True)
    isopado = models.BooleanField('Isopado', null = True)
    fecha_isopado = models.DateTimeField('Fecha de isopado', null = True)

    def __str__(self):
        return f'Solicitante {self.first_name}, {self.last_name}'
        

class Permiso(models.Model):
    #Opciones para crear model que solo acepte estos tipos
    choices_estado = [
        ('sinAdmin', 'Permiso solicitado'),
        ('conAdmin', 'Permiso en revision'), 
        ('aprobado', 'Permiso aprobado'),
        ('rechazado', 'Permiso rechazado'),
        ]
    choices_tipoPermiso = [
        ('caminata','Caminata'),
        ('compras','Compras'),
        ('mudanza', 'Mudanza'),
        ('visitaMedica','Visita medica'),
        ('viaje','Viaje')
        ]
    #Model
    id = models.IntegerField(primary_key = True)
    user = models.OneToOneField(Ciudadano, on_delete=models.CASCADE)
    administrador_id = models.OneToOneField(User, on_delete = models.CASCADE, blank=True)
    tipo_permiso = models.CharField(max_length=15, choices = choices_tipoPermiso)
    estado = models.CharField(max_length = 20, choices = choices_estado, default = 'sinAdmin')
    detalle = models.CharField(max_length = 256, blank = True, null = True)
    motivo = models.CharField(max_length = 256, blank = True, null = True)

    def __str__(self):
        return f'Permiso: {self.tipo_permiso}'
