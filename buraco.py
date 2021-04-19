# coding: utf-8
import pygame
import random
from config import *
from pygame.locals import *


class Buraco(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(IMAGEM_BURACO)
        self.rect_buraco = self.image.get_rect()
        self.pista = [145, 255, 355]
        self.speed = 5
    
    def move(self):
        self.y += self.speed
        if self.y > 600:
            self.y = -self.speed
            self.x = self.pista[random.randint(0, 2)]
        
        self.rect_buraco.y = self.y
        self.rect_buraco.x = self.x  
        
    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.rect_buraco.normalize()