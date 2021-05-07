
import pygame
import random
from config import *
from pygame.locals import *


def aumentar_velocidade(score, carros_inimigos, carro, background_speed, temp_maximo):
    if score % 100 == 0 and score != 0:
        carros_inimigos[0].speed += 0.5
        carros_inimigos[1].speed += 0.5
        carro.speed += 0.2
        background_speed += 0.3
        if score > 200:
            temp_maximo -= 1.3


def local_pista():  
    pista = [140, 255, 355]
    pista_atual = pista[random.randint(0, 2)]
    
    return pista_atual


def mover_backgroud(screen,imagem_1, imagem_2, y):
    screen.blit(imagem_1, (0, y))
    screen.blit(imagem_2, (0, y - RESOLUCAO[1]))


def musica(estado):
    if estado == 1:
        pygame.mixer.music.load(CAMINHO_DA_MUSICA)
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.stop()


def efeitos_sonoros(tipo):
    if tipo == "Game_Over":
        game_over = pygame.mixer.Sound(CAMINHO_DA_MUSICA_GAMEOVER)
        game_over.play()
    elif tipo == "Retorno":
        retorno = pygame.mixer.Sound(CAMINHO_DA_MUSICA_RETORNO)
        retorno.play()            
    elif tipo == "Click":
        click = pygame.mixer.Sound(CAMINHO_DA_MUSICA_SELECIONAR)
        click.play()


def imprime_texto(screen, texto, posicao, fonte, cor):
    mensagem = fonte.render(str(texto), True, cor)
    screen.blit(mensagem, posicao)


def salvar_score(score):
    ultimo_recorde = open(ARQUIVO_SALVA_SCORE, "r").read()
    
    if int(score) > int(ultimo_recorde):
        texto = open(ARQUIVO_SALVA_SCORE, "w")
        texto.write(str(score))     


def intro(situ):
    if situ == 1:
        pygame.mixer.music.load(INTRO)
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.stop()
       
def fechar_janela():
    pygame.quit()
    sys.exit()
