import pygame
from pygame import Vector2

from Camera import Camera
from square import Square
from midi import list_notes_from_midi
from utils import utils


class Explosion:
    def __init__(self, pos, image):
        self.pos = pos
        self.timer = 0
        self.duration = 1
        self.image = image
        self.size = image.get_width()

    def update(self, dt):
        self.timer += dt
        self.size += 100 * dt 

    def draw(self, screen, camera):
       
        scaled_img = pygame.transform.scale(self.image, (int(self.size), int(self.size)))
        
        pos = camera.apply_pos(self.pos) - Vector2(self.size / 2, self.size / 2)
        screen.blit(scaled_img, pos)

    def is_done(self):
        return self.timer >= self.duration


class Game:
    def __init__(self):
        self.all_notes = list_notes_from_midi("you.mid")
        print(self.all_notes)

        self.square = Square(Vector2(10, utils.height / 2))
        self.camera = Camera(utils.width, utils.height)
        self.camera.set_target(self.square)

        self.points = []

        self.time = 0
        self.fixedDeltaTime = 0.016

        
        self.point_image = pygame.image.load("rick.png").convert_alpha()

        
        self.explosions = []

    def update(self):
        self.time += self.fixedDeltaTime

        for note in self.all_notes:

            
            if note["start_time"] <= self.time and not note["play"] and note["velocity"] > 0:
                note["play"] = True

                if self.square.vel.y < 0:
                    pos = Vector2(self.square.pos.x, self.square.pos.y)
                else:
                    pos = Vector2(self.square.pos.x, self.square.pos.y + self.square.width)

                self.square.vel.y *= -1

              
                self.explosions.append(Explosion(pos, self.point_image))

                utils.player.note_on(
                    note["name"],
                    min(note["velocity"] * utils.volumeScale, 127)
                )

          
            if note["start_time"] <= self.time and not note["play"] and note["velocity"] == 0:
                note["play"] = True
                utils.player.note_off(note["name"], 0)

        self.square.update(self.fixedDeltaTime)
        self.camera.update()

    
        for explosion in self.explosions[:]:
            explosion.update(self.fixedDeltaTime)
            if explosion.is_done():
                self.explosions.remove(explosion)

    def draw(self):
       
        for explosion in self.explosions:
            explosion.draw(utils.screen, self.camera)

        
        for p in self.points:
            pos = self.camera.apply_pos(Vector2(p.x, p.y))
            img_rect = self.point_image.get_rect(center=pos)
            utils.screen.blit(self.point_image, img_rect)

        self.square.draw(self.camera)
