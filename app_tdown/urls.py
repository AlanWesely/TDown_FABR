from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),     # Acessa a Tela Home
    path('cadastro-partida/<id>/', views.cadPartida),  # Acessa a Tela Cadastro de Partida
    path('cadastro-jogada/', views.cadJogada),    # Acessa a Tela Cadastro de Jogadas
    path('cadastro-time/', views.cadTime)  # Acessa a Tela Cadastro de Times
]