from django.urls import path
from OtroGrupo import views

urlpatterns = [
	path("", views.home),
    path("home/", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("register/", views.register, name='register'),
    path("logout/", views.logout, name='logout'),
    path("perfil/", views.perfil, name='perfil'),
    path("registro_exitoso/", views.registro_exitoso),
]