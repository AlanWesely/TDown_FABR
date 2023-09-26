from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'app_tdown/pages/home.html')


def cadPartida(request):
    return HttpResponse('cadPartida')  # Cadastro de Partida


def cadJogada(request):
    return HttpResponse('cadJogada')  # Cadastro das Jogadas


def cadTime(request):
    return HttpResponse('cadTime')  # Cadastro das Times