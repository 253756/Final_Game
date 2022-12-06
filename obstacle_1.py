import pygame
import random

class Obstacle1(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('images/rain_drop.png')
        self.rect = self.image.get_rect()
        self.x = random.randint(0,640)
        self.y = -30
        self.speed = 1

    def update(self):
        self.rect.y += 1
        if self.rect.top > self.screen.get_rect().bottom:
            self.rect.bottom = 0

   # def random(self):
        ##if self.rect.top > self.screen.get_rect().bottom:

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    #def drop(self, speed):
    #    self.position[1] += speed

    #def draw(self, surface):
       # pygame.draw.circle(surface,(0,0,0), self.position, self.size)
        #surface.blit(self.image, self.rect)
clock = pygame.time.Clock()