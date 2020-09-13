from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'index.html', {})


def login(request):
	return render(request, 'login.html', {})


def perfil(request):
	return render(request, 'perfil.html', {})