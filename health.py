import pygame
import random
from ship_1 import Ship1
from ship_2 import Ship2


class Health(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        #screen for game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        #image for health
        self.image = pygame.image.load('images/dead_ship.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 620)
        self.rect.y = -30
        self.player1 = Ship1(game)
        player2 = Ship2(game)
    def update(self):
        """speed of health that comes down"""
        self.rect.y += self.settings.life_speed
        if self.rect.bottom == self.screen.get_rect().bottom:
            self.rect.bottom = 0

    def draw(self):
        """brings the image onto the screen"""
        self.screen.blit(self.image, self.rect)


