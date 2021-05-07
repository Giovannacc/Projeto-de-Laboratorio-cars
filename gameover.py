import pygame
import sys
import interface
from function import *
from config import *
from pygame.locals import *


def game_over(screen, score):    
    inter = interface.interface(screen)
    game_over = pygame.image.load(FIM) 
    trofeu = pygame.image.load(TROFEU)
    ultimo_recorde = open(ARQUIVO_SALVA_SCORE, "r").read()


    efeitos_sonoros("Game_Over")
    intro(1)
    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
               fechar_janela()

        screen.blit(game_over, (0, 0))
        if score >= int(ultimo_recorde):
            imprime_texto(screen, "NOVO  RECORDE", (197, 210), FONTE_PIXEL, BRANCO)
            imprime_texto(screen, score, (255, 240), FONTE_DG, BRANCO)
            screen.blit(trofeu, (230, 280))
        else:
            imprime_texto(screen, "seu score", (77, 210), FONTE_PIXEL, BRANCO)
            imprime_texto(screen, score, (133, 240), FONTE_DG, BRANCO)
            imprime_texto(screen, "maior score", (277, 210), FONTE_PIXEL, BRANCO)
            imprime_texto(screen, ultimo_recorde, (356, 240), FONTE_DG, BRANCO)
        
        imprime_texto(screen, "TENTE NOVAMENTE...", (152, 388), FONTE_DG, BRANCO)
        imprime_texto(screen, "PRESSIONE   ENTER", (90, 540), FONTE_PIXEL2, PRETO)
        
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_RETURN]:
            inter.menu(screen)

        
        pygame.display.flip()
