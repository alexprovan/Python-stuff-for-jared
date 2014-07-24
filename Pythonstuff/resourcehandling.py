__author__ = 'ProvanAlex'
try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    import shelve
    import objects
    import gameplayfunctions
    from socket import *
    from pygame.locals import *
except ImportError:
    print("couldn't load module. %s")

class startup:
    def save_game(self, savegame):
        fullname = os.path.join('saves', savegame)
        savefile = shelve.open(fullname)
        savefile['playerstats'] = playerstats
        savefile['playertile'] = playertile
        savefile['enemytile'] = enemytile
        savefile.close()
        return savefile

    def load_game(self, savegame):
        """
    Loads the safegame from the disk
        :param savegame:
        """
        fullname = os.path.join('saves', savegame)
        savefile = shelve.open(fullname)
        playerstats = savefile['playerstats']
        playertile = savefile['playertile']
        enemytile = savefile['enemytile']
        savefile.close()

