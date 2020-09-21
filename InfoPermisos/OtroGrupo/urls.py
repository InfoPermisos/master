from django.urls import path
from OtroGrupo import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("login/", views.login, name= 'login'),
    path("register/", views.register, name= 'register'),
    path("perfil/", views.perfil, name= 'perfil'),
    path("solicitud/", views.solicitud, name= 'solicitud'),
    path("permisor/", views.permisor_general, name= 'permisor'),
    path("permisor/revision/", views.permisor_revision, name= 'permisor_revision'),
    path("permisor/masDetalles/", views.permisor_masDetalles, name= 'permisor_detalles'),
]