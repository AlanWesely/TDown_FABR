from django.urls import path
from app_tdown.views import home, cadPartida, cadJogada, cadTime


urlpatterns = [
    path('', home),     # Acessa a Tela Home
    path('cadastro-partida/', cadPartida),  # Acessa a Tela Cadastro de Partida
    path('cadastro-jogada/', cadJogada),    # Acessa a Tela Cadastro de Jogadas
    path('cadastro-time/', cadTime)  # Acessa a Tela Cadastro de Times
]