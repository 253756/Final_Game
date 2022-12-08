import pygame.font
from pygame.sprite import Group


class Score:
    def __init__(self, game):
        #ethan helped with score
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.player1 = game.player1
        self.player2 = game.player2

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_level()
        self.player1_score()
        self.player2_score()

    # It Shows the Current Game Level
    def prep_level(self):
        level_str = str(self.settings.level)
        self.level_image = self.font.render(level_str, True,
        self.text_color, self.settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right -20
        self.level_rect.top = 20
    def player1_score(self):
        player1_str = str(self.player1.health)
        self.player1_image = self.font.render(player1_str, True,
        self.text_color, self.settings.bg_color)
        # Position the level below the score.
        self.player1_rect = self.player1_image.get_rect()
        self.player1_rect.left = self.screen_rect.left +5
        self.player1_rect.top = 20
    def player2_score(self):
        player2_str = str(self.player2.health)
        self.player2_image = self.font.render(player2_str, True,
        self.text_color, self.settings.bg_color)
        # Position the level below the score.
        self.player2_rect = self.player2_image.get_rect()
        self.player2_rect.left = self.screen_rect.left +5
        self.player2_rect.top = 60
    def show(self):
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.player1_image,self.player1_rect)
        self.screen.blit(self.player2_image, self.player2_rect)


