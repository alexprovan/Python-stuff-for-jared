__author__ = 'ProvanAlex'
import objects
import sys
import random
import math
import os
import getopt
import pygame
import shelve
import objects
import operator
from socket import *
from pygame.locals import *
from pygame import Surface
from types import *
from objects import races

class charactercreation(object):
    def __init__(self):
        playername = input("What is your name Traveler? ")
        list(objects.races.keys())
        playerrace = input("choose your race ")
        list(objects.chclasses.keys())
        playerclass = input("choose your class ")
        playerracestats = objects.races[playerrace]
        playerclassstats = objects.chclasses[playerclass]
        self.playersbasekill = tuple(map(sum, zip(playerclassstats['skill'], playerracestats['skill'])))
        self.playerbasestat = tuple(map(sum, zip(playerclassstats['stat'], playerracestats['stat'])))
    def returnskill(self):
        stat = self.playerbasestat
        skill = self.playersbasekill
        return skill, stat













