import pygame
import sys

class Ship2:
    def __init__(self):
        self.image = pygame.image.load("images/ship2.png")
        self.dead_image = pygame.image.load('images/dead_ship2.png')
        self.rect = self.image.get_rect()
        # movement flags
        self.health = 1000

    def draw(self, surface):
        if self.health <=300:
            self.image = self.image
        if self.health <= 0:
            self.image = self.dead_image
        surface.blit(self.image, self.rect)

    def move(self, coordinate):
        self.rect.center = coordinate