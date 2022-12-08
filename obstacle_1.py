import pygame
import random


class Obstacle1(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('images/rain_drop.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 620)
        self.rect.y = 20
        #self.speed = 6
        self.y = float(self.rect.y)

    def update(self):
        self.rect.y += self.settings.obstacle_speed
        if self.rect.top > self.screen.get_rect().bottom:
            self.rect.bottom = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)


