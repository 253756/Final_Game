import pygame

class Button():
    def __init__(self, game):
        #screen
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #image for button
        self.image = pygame.image.load("images/start_button.png")

        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def draw_button(self):
        """brings the button onto the screen"""
        self.screen.blit(self.image, self.rect)

