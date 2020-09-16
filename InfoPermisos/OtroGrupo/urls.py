from django.urls import path
from OtroGrupo import views

urlpatterns = [
    path("home/", views.home),
    path("login/", views.login),
    path("register/", views.register),
    path("perfil/", views.perfil),
    path("registro_exitoso/", views.registro_exitoso),
]