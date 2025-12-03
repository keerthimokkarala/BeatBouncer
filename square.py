import pygame
from pygame import Vector2
from utils import utils


class Square:
    def __init__(self, pos, image_path="ball.PNG"):

        self.image = pygame.image.load(image_path).convert_alpha()


        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.pos = Vector2(pos)
        self.vel = Vector2(550, 800)

        # Trail
        self.trail = []
        self.trail_lifetime = 10

    def getRect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)

    def update(self, deltaTime):

        self.trail.append(self.pos.copy())
        if len(self.trail) > self.trail_lifetime:
            self.trail.pop(0)


        self.pos += self.vel * deltaTime

    def draw(self, camera):

        for i, pos in enumerate(reversed(self.trail)):
            alpha = 255 * (1 - i / self.trail_lifetime)

            faded = self.image.copy()
            faded.set_alpha(alpha)

            p = camera.apply_pos(pos)
            utils.screen.blit(faded, (p.x, p.y))


        p = camera.apply_pos(self.pos)
        utils.screen.blit(self.image, (p.x, p.y))