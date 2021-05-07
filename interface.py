
import pygame
import sys
from config import *
from pygame.locals import *
from nivel1 import *
from nivel2 import *
from animed import *


class interface:
    def __init__(self, screen):
        self.nivel1 = pygame.image.load("img/jogar.png")
        self.op_controles = pygame.image.load("img/op_controle.png")
        self.op_creditos = pygame.image.load("img/op_creditos.png")
        self.nivel2 = pygame.image.load("img/nivel2.png")
        self.buton = pygame.image.load("img/subtela.png")
        self.rect_nivel1 = self.nivel1.get_rect()
        self.rect_nivel1.x, self.rect_nivel1.y = 136, 156
        self.rect_nivel2 = self.nivel2.get_rect()
        self.rect_nivel2.x, self.rect_nivel2.y = 136, 246
        self.rect_controles = self.op_controles.get_rect()
        self.rect_controles.x, self.rect_controles.y = 136, 336
        self.rect_creditos = self.op_creditos.get_rect()
        self.rect_creditos.x, self.rect_creditos.y = 136, 416
        self.rect_buton = self.buton.get_rect()
        self.rect_buton.x, self.rect_buton.y = 10, 10

    def atualiza_imagem(self, screen, imagem):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar_janela()

            self.posicao_mouse = pygame.mouse.get_pos()
            screen.blit(imagem, (0, 0))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RETURN]:
                efeitos_sonoros("Retorno")
                break
            pygame.display.flip()

    def atualiza_imagem_mouse(self, screen, imagem, rect, funcao):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar_janela()

                self.posicao_mouse = pygame.mouse.get_pos()
                if not rect.collidepoint((self.posicao_mouse)): return
                screen.blit(imagem, (0, 0))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN:
                    efeitos_sonoros("Click")
                    funcao(screen)

    def iniciar_jogo(self, screen):
        imagem_inicial = pygame.image.load(SUBTELA)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar_janela()

            screen.blit(imagem_inicial, (0, 0))
            pygame.display.flip()

            if self.rect_buton.collidepoint(pygame.mouse.get_pos()):
                imagem_enter = pygame.image.load(SUBTELA)
                self.atualiza_imagem_mouse(screen, imagem_enter, self.rect_buton, obj)

    def controles(self, screen):
        menu_controles = pygame.image.load(CONTROLS)
        self.atualiza_imagem(screen, menu_controles)

    def creditos(self, screen):
        menu_creditos = pygame.image.load(CREDIT)
        self.atualiza_imagem(screen, menu_creditos)

    def menu(self, screen):

        imagem_menu_inicial = pygame.image.load(IMAGEM_MENU)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar_janela()

            screen.blit(imagem_menu_inicial, (0, 0))
            pygame.display.flip()
            self.posicao_mouse = pygame.mouse.get_pos()


            if self.rect_nivel1.collidepoint(self.posicao_mouse):
                imagem_nivel1 = pygame.image.load(SELECIONADO_JOGAR)
                self.atualiza_imagem_mouse(screen, imagem_nivel1, self.rect_nivel1, main)

            elif self.rect_controles.collidepoint(self.posicao_mouse):
                imagem_controles = pygame.image.load(SELECIONADO_CONTROLES)
                self.atualiza_imagem_mouse(screen, imagem_controles, self.rect_controles, self.controles)


            elif self.rect_creditos.collidepoint(self.posicao_mouse):
                imagem_creditos = pygame.image.load(SELECIONADO_CREDITOS)
                self.atualiza_imagem_mouse(screen, imagem_creditos, self.rect_creditos, self.creditos)


            else:
                self.rect_controles.collidepoint(self.posicao_mouse)
                imagem_nivel2 = pygame.image.load(SELECIONADO_JOGAR2)
                self.atualiza_imagem_mouse(screen, imagem_nivel2, self.rect_nivel2, main2)

