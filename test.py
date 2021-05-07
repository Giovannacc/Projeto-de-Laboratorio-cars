import pytest
import config
from nivel1 import *
from function import *
import interface

# TESTE CAIXA BRANCA


def test_salvar_score():
    ultimo_recorde = 10
    score = 100
    if int(score) > int(ultimo_recorde):
        ultimo_recorde = score

    assert ultimo_recorde == 100


def test_salvar_score2():
    ultimo_recorde = 1
    score = 10
    if int(score) > int(ultimo_recorde):
        ultimo_recorde = score

    assert ultimo_recorde == 10


def test_efeitos_sonoros():
    tipo = "Game_Over"
    game_over = pygame.mixer.Sound(CAMINHO_DA_MUSICA_GAMEOVER)
    assert game_over.play(tipo)


def test_efeitos_sonoros1():
    tipo = "Retorno"
    retorno = pygame.mixer.Sound(CAMINHO_DA_MUSICA_RETORNO)
    assert retorno.play(tipo)


def test_efeitos_sonoros2():
    tipo = "Click"
    click = pygame.mixer.Sound(CAMINHO_DA_MUSICA_SELECIONAR)
    assert click.play(tipo)
