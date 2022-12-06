import pygame
import random
class Health():
    def __init__(self, screen,x,y):
        super().__init__()
        self.screen = screen
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('images/obstacle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = random.randint(0,640)
        self.y = -60
    def draw(self, screen):
        screen.blit(self.image, self.rect)
