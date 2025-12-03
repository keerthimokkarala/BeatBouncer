import pygame
from utils import utils
from game import Game

pygame.display.set_caption("Beat Bouncer")
background = pygame.image.load("space.png").convert()

game = Game()


while True:

    utils.screen.blit(background, (0, 0))


    utils.initDeltaTime()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


    game.update()
    game.draw()


    pygame.display.flip()
