
import pygame
import random
from config import *
from pygame.locals import *


class CarroInimigo(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(IMAGEM_CARRO_INIMIGO)
        self.rect_carro = self.image.get_rect()
        self.pista = [140, 254, 355]
        self.speed = 6.5
    
    def move(self):
        self.y += self.speed
        if self.y > 600:
            self.y = -self.speed
            self.x = self.pista[random.randint(0, 2)]
        
        self.rect_carro.y = self.y
        self.rect_carro.x = self.x     
    
    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.rect_carro.normalize()