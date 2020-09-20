from django.urls import path
from OtroGrupo import views

urlpatterns = [
    path("home/", views.home),
    path("login/", views.login),
    path("register/", views.register),
    path("perfil/", views.perfil),
    path("solicitud/", views.solicitud),
    path("permisor/", views.permisor_general),
    path("permisor/revision/", views.permisor_revision),
    path("permisor/masDetalles/", views.permisor_masDetalles),
]