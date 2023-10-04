from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),     # Acessa a Tela Home
    path('cadastro-partida/<id>/', views.cadPartida),  # Acessa Cad de Partida
    path('visualizar-partida/<id>/', views.viewPartida),  # Acessa Vis Partida
    path('cadastro-jogada/', views.cadJogada),    # Acessa Tela Cad de Jogadas
    path('cadastro-time/', views.cadTime)  # Acessa a Tela Cadastro de Times
]
