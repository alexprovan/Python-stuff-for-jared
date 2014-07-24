__author__ = 'ProvanAlex'
import sys
import os
import configparser
import pygame as pg
from pygame.locals import *

screensize = (800, 800)
directdict = {pg.K_LEFT: (-1, 0),
              pg.K_RIGHT: (1, 0),
              pg.K_UP: (0, -1),
              pg.K_DOWN: (0, 1)}
class Player(object):
    def __init__(self, rect, speed, image):
        self.rect = pg.Rect(rect)
        self.speed = speed
        self.image = self.make_image(image)

    def make_image(self, image):
        image = pg.image.load(image)
        image = pg.transform.scale(image, (25, 25))
        return image
    def update(self, screen_rect, keys):
        for key in directdict:
            if keys[key]:
                self.rect.x += directdict[key][0] * self.speed
                self.rect.y += directdict[key][1] * self.speed
                self.rect.clamp(screen_rect)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Tiles(object):
    def __init__(self, imagefile, width, height):
        image = pg.image.load(imagefile)
        image_width, image_height = image.get_size()
        self.image_width = image_width
        self.image_height = image_height
        self.image = image
        self.width = width
        self.height = height

    def load_tile_table(self):
        image = self.image
        tile_table = []
        for tile_x in range(0, self.image_width / self.width):
            line = []
            tile_table.append(line)
            for tile_y in range(0, self.image_height / self.height):
                rect = (tile_x * self.width, tile_y * self.height, self.width, self.height)
                line.append(image.subsurface(rect))
        return tile_table

class Gamemap(object):
    def __init__(self, filename, mapname):
        self.map = {}
        self.key = []
        self.width = width
        self.height = height

    def mapcreate(self, filename, mapname):
        mapx = []
        gamemap = []
        mapxy = []
        parser = configparser.ConfigParser()
        parser.read(filename)
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.desc = desc
            else:
                leveldescriptiondict = dict(parser.items(section))
                self.leveldescriptiondict = leveldescriptiondict
        mapfile = open(mapname, 'r')
        for line in mapfile:
            gamemap.append(line)
        mapy = dict(enumerate(gamemap)).keys()
        for x in gamemap[0]:
            if type(gamemap[0]) is str:
                mapx.append(gamemap[0].index(x))
            else:
                print("this map is not a valid map")
        mapxy = zip(mapx, mapy)

    def get_tile(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError:
            return {}
        try:
            return self.key[char]
        except KeyError:
            return {}

class Control(object):
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_caption("move me with the arrow keys")
        self.screen = pg.display.set_mode(screensize)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed()
        self.player = Player((0, 0, 100, 100), 5, "character.png")
    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == pg.QUIT or self.keys[K_ESCAPE]:
                self.done = True
    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.player.update(self.screen_rect, self.keys)
            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            pg.display.update()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pg.quit()
    sys.exit()

