from django.urls import path
from OtroGrupo import views

urlpatterns = [
	#URLS generales
    path("home/", views.home),
    path("login/", views.login),
    path("register/", views.register),
    #URLS del permisor
    path("permisor/", views.permisor_general),
    path("permisor/revision/", views.permisor_revision),
    path("permisor/masDetalles/", views.permisor_masDetalles),
    #URLS
    path("estado/", views.estado),
    path("perfil/", views.perfil),
    path("solicitud/", views.solicitud),
    path("historial/", views.historial),
]