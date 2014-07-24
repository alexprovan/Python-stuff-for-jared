import objectclasses
import resourcehandling
import gameplayfunctions
import objects
import pygame
from resourcehandling import startup
from objectclasses import Player
from pygame.locals import *


def main():
    """

    :rtype : Player Object
    """
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    clock = pygame.time.Clock()
    player = objectclasses.Player()
    playersprite = pygame.sprite.RenderClear(player)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    playersprite.move_right()
                if event.key == K_d:
                    playersprite.move_left()
                if event.key == K_w:
                    playersprite.move_up()
                if event.key == K_s:
                    playersprite.move_down()
            elif event.type == KEYUP:
                playersprite.movepos = [0, 0]
                playersprite.state = "still"
main()



