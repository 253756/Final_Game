import pygame
import sys

class Ship1:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the Basket image
        self.image = pygame.image.load('images/ship1.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the decimal value for the basket's horizontal position.
        self.x = float(self.rect.x)
        self.health = 1000

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        #set the boundaries!!

    #def draw(self, surface):
     #   if self.health <=300:
      #      self.image = self.image
       # if self.health <= 0:
        #    self.image = self.dead_image
        #surface.blit(self.image, self.rect)

    def move(self, coordinate):
        self.rect.center = coordinate

    def blitme(self):
        """Draw the basket at its current location"""
        self.screen.blit(self.image, self.rect)