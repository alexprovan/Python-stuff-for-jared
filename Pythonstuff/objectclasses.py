__author__ = 'ProvanAlex'
import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
import gameplayfunctions
import objects
import resourcehandling
from resourcehandling import startup
class gamesprite(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = startup.load_png(self, image)
