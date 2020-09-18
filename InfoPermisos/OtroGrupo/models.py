from django.db import models

class Usuario(models.Model):
    dni = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    clave = models.CharField(max_length = 100)


class Ciudadano(models.Model):
    id = models.IntegerField(primary_key=True)
    dniId = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaNacimiento = models.DateTimeField(blank = True)
    ciudad = models.CharField(max_length = 126)
    empleo = models.CharField(max_length = 126)
    enfermedades = models.CharField(max_length = 126)
    isopado = models.BooleanField()
    fechaIsopado = models.DateTimeField(blank = True, null = True)


class Administrador(models.Model):
    id = models.IntegerField(primary_key=True)
    dniId = models.ForeignKey(Usuario, on_delete = models.CASCADE)


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
    ciudadanoId = models.ForeignKey(Ciudadano, on_delete = models.CASCADE)
    administradorId = models.ForeignKey(Administrador, on_delete = models.CASCADE, blank=True)
    tipoPermiso = models.CharField(max_length=15, choices = choices_tipoPermiso)
    estado = models.CharField(max_length = 20, choices = choices_estado, default = 'sinAdmin')
    detalle = models.CharField(max_length = 256, blank = True, null = True)
    motivo = models.CharField(max_length = 256, blank = True, null = True)