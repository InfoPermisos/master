from django.urls import path
from OtroGrupo import views

urlpatterns = [
    path("home/", views.home),
    path("login/", views.login),
    path("register/", views.register),
    path("perfil/", views.perfil),
    path("solicitud/", views.solicitud),
]