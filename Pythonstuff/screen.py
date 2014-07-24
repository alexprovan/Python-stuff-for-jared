__author__ = 'ProvanAlex'
import pygame
from pygame import time
from pygame.locals import *
screen = pygame.display.set_mode((700, 700))
background = pygame.Surface(screen.get_size())
background = background.convert()
clock = pygame.time.Clock()
background.fill((250, 250, 250))
screen.blit(background, (0, 0))
pygame.display.flip()
while 1:
    clock.tick(60)