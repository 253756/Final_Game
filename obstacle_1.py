import pygame
import random


class Obstacle1(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        #screen
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        #image for obstacle
        self.image = pygame.image.load('images/rain_drop.png')
        self.rect = self.image.get_rect()

        #starting positions
        self.rect.x = random.randint(0, 620)
        self.rect.y = 20
        self.y = float(self.rect.y)

    def update(self):
        """controls speed that it falls at and the boundary"""
        self.rect.y += self.settings.obstacle_speed
        if self.rect.top > self.screen.get_rect().bottom:
            self.rect.bottom = 0

    def draw(self):
        """brings obstacle onto the screen"""
        self.screen.blit(self.image, self.rect)


