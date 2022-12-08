import pygame
import sys

class Ship2:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the Basket image
        self.image = pygame.image.load('images/ship2.png')
        self.dead_image = pygame.image.load('images/dead_ship2.png')

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the decimal value for the basket's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        self.health = 1000

    def move(self, coordinate):
        self.rect.center = coordinate

    def blitme(self):
        if self.health <= 300:
            self.image = self.image
        if self.health <= 0:
            self.image = self.dead_image
        self.screen.blit(self.image, self.rect)
    def updates(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 3
        if self.moving_left and self.rect.left > 0:
            self.x -= 3
        # Update rect object from self.x
        self.rect.x = self.x