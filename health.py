import pygame
import random
from ship_1 import Ship1
from ship_2 import Ship2


class Health(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('images/dead_ship.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 620)
        self.rect.y = -30
        self.speed = 5
        self.player1 = Ship1(game)
        self.player2 = Ship2(game)

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom == self.screen.get_rect().bottom:
            self.player1.health -= 50
            self.player2.health -= 50
            self.rect.bottom = 0



    def draw(self):
        self.screen.blit(self.image, self.rect)


