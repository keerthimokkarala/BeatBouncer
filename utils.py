import colorsys

import pygame

from pygame.locals import *

from pygame import time
import pygame.midi



class Utils():

    def __init__(self):

        pygame.init()

        self.width = 1000
        self.height = 800

        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF, 16)
        self.dt = 0
        self.clock = pygame.time.Clock()

        pygame.midi.init()
        self.volumeScale = 10
        self.player = pygame.midi.Output(0)

    def initDeltaTime(self):
        t = self.clock.tick(60)
        self.dt = t / 1000

    def deltaTime(self):
        return self.dt

    def hueToRGB(self, hue):

        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

        return (int(r * 255), int(g * 255), int(b * 255))


utils = Utils()