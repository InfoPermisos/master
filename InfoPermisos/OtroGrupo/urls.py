from django.urls import path
from OtroGrupo import views

urlpatterns = [

	path("home/", views.home),
	path("login/", views.login),
	path("perfil/", views.perfil)
]