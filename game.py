import pygame
from config import *
from pygame.locals import *
from interface import *

pygame.init()
windows = pygame.display.set_mode(RESOLUCAO, 0, 32)
screen = pygame.display.get_surface()
pygame.display.set_caption("Game Combat")
Icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(Icon)


interface = interface(screen)
interface.iniciar_jogo(screen)
interface.menu(screen)
