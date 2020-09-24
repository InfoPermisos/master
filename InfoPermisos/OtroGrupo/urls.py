from django.urls import path
from OtroGrupo import views

urlpatterns = [
	path('', views.home, name='home'),
    path("home/", views.home, name='home'),
    path("login/", views.login, name= 'login'),
    path("logout/", views.logout, name= 'logout'),
    path("register/", views.register, name= 'register'),
    path("perfil/", views.perfil, name= 'perfil'),
    path("perfil_form/", views.perfil_form, name= 'perfil_form'),
    path("solicitud/", views.solicitud, name= 'solicitud'),
    path("detalles_guardados/", views.detalles_guardados, name= 'detalles_guardados'),
    path("estado/", views.estado, name= 'estado'),
    path("historial/", views.historial, name='historial'),
    #Permisor
    path("permisor/", views.permisor_general, name= 'permisor'),
    path("permisor/revision/", views.permisor_revision, name= 'permisor_revision'),
    path("permisor/masDetalles/", views.permisor_masDetalles, name= 'permisor_detalles'),
]