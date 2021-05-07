import pygame
import sys
from function import *
from config import *
from carro import *
from gameover import *
from pygame.locals import *
import interface
from function import *


def animed_over(screen):
    inter = interface.interface(screen)
    ani_over = pygame.image.load("img/comando.png")

    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_janela()
        screen.blit(ani_over, (0, 0))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            inter.menu(screen)


        pygame.display.flip()


def obj(screen):

    imagem_1 = pygame.image.load("img/setas.png")
    imagem_2 = pygame.image.load("img/desvio.png")
    posicao_y = 0
    carro = Carro(screen)
    tempo = 0
    cont_tempo = 0
    tela_speed = 1
    intro(1)

    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tecla = pygame.key.get_pressed()

        # ANIMAÇAO BACKGROUND #
        mover_backgroud(screen, imagem_1, imagem_2, posicao_y)
        posicao_y += tela_speed
        if posicao_y >= RESOLUCAO[1]:
            posicao_y = 0

        cont_tempo += 1
        if cont_tempo % 6 == 0:
            tempo += 1

        if tempo == 100:
            animed_over(screen)

        carro.render()
        carro.mover_carro(tecla)

        pygame.display.flip()
