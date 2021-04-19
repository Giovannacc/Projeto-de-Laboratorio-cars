# coding: utf-8
import pygame
from config import *
from pygame.locals import *


class Carro(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.imagem_do_carro = pygame.image.load(IMAGEM_CARRO)
        self.rect_car = self.imagem_do_carro.get_rect()
        self.posicao = (255, 460)
        self.life = 3
        self.speed = 4
        self.rect_car.x, self.rect_car.y = (255, 460)
        
    def mover_carro(self, tecla):
        if tecla[pygame.K_LEFT]:
            x = self.posicao[0] - self.speed
            if x <= 105:
                x = 110
            self.posicao = (x, self.posicao[1])
            self.rect_car.x = x
            self.rect_car.y = self.posicao[1]
        
        elif tecla[pygame.K_RIGHT]:
            x = self.posicao[0] + self.speed
            if x >= 385:
                x = 380
            self.posicao = (x, self.posicao[1])
            self.rect_car.x = x
            self.rect_car.y = self.posicao[1]
        
        elif tecla[pygame.K_UP]:
            y = self.posicao[1] - self.speed
            if y <= 0:
                y = 5
            self.posicao = (self.posicao[0], y)
            self.rect_car.x = self.posicao[0]
            self.rect_car.y = y
        
        elif tecla[pygame.K_DOWN]:
            y = self.posicao[1] + 6
            if y >= 480:
                y = 480
            self.posicao = (self.posicao[0], y)
            self.rect_car.x = self.posicao[0]
            self.rect_car.y = y
                                  
    def render(self):
        self.screen.blit(self.imagem_do_carro, self.posicao)
        self.rect_car.normalize()