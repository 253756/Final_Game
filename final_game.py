import pygame
import sys
from ship_1 import Ship1
import random
from obstacle_1 import Obstacle1
from health import Health
from ship_2 import Ship2
from button import Button


class Final():
    def __init__(self):
        pygame.init()
        self.background_tile = pygame.image.load("images/water_tile.png")
        self.water_rect = self.background_tile.get_rect()
        self.tile_size = self.water_rect.width
        self.screen = pygame.display.set_mode((10*self.tile_size,10*self.tile_size))
        self.screen.fill((0,0,0))
        self.screen_rect = self.screen.get_rect()
        self.rows = self.screen_rect.height//self.tile_size
        self.cols = self.screen_rect.width//self.tile_size
        self.clock = pygame.time.Clock()
        self.obstacles = pygame.sprite.Group()
        self.button = Button(320,320)

        #bring in players
        self.player1 = Ship1(self)
        self.player2 = Ship2(self)

    def run_game(self):
        self._check_events()
        self._ship_1_check()
        self._ship_2_check()
        self._player1_and_obstacle_collision()
        self._player2_and_obstacle_collision()
        self._check_obsatcles_bottom()
        self._drop_obstacles()
        self.clock.tick(100)
        self.update()
        self.player1.update()
        pygame.display.flip()

    #drawing my ocean on the screen
    def update(self):
        for x in range(int(self.rows)):
            for y in range(int(self.cols)):
                self.screen.blit(self.background_tile, (x*self.water_rect.height, y*self.water_rect.width))
        self.player1.blitme()
        self.player2.blitme()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _ship_1_check(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player1.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.player1.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player1.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.player1.moving_left = False
    def _ship_2_check(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player2.moving_up = True
                elif event.key == pygame.K_a:
                    self.player2.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player2.moving_up = False
                elif event.key == pygame.K_a:
                    self.player2.moving_down = False
    def _player1_and_obstacle_collision(self):
        collisions = pygame.sprite.spritecollide(self.player1, self.obstacles, True)
        if collisions:
            # If collision detected add a point
            self.player1.health -= 50

    def _player2_and_obstacle_collision(self):
        collisions = pygame.sprite.spritecollide(self.player2, self.obstacles, True)
        if collisions:
            # If collision detected add a point
            self.player2.health -= 50

    def _check_obsatcles_bottom(self):
        '''It checks if the apple crosses the screen bottom'''
        screen_rect = self.screen.get_rect()
        for obstacle in self.obstacles.sprites():
            if obstacle.rect.bottom >= screen_rect.bottom:
                break

    def _drop_obstacles(self):
        '''Drop apples from the top, randomly'''
        if len(self.obstacles) == 0:
                new_obstacle = Obstacle1(self)
                self.obstacles.add(new_obstacle)
        if len(self.obstacles) == 1:
            for obstacle in self.obstacles.sprites():
                if obstacle.rect.bottom > 300:
                    new_obstacle = Obstacle1(self)
                    self.obstacles.add(new_obstacle)
        if len(self.obstacles) == 2:
            for obstacle in self.obstacles.sprites():
                if obstacle.rect.bottom > 600:
                    new_obstacle = Obstacle1(self)
                    self.obstacles.add(new_obstacle)
        if len(self.obstacles) == 3:
            for obstacle in self.obstacles.sprites():
                if obstacle.rect.bottom > 900:
                    new_obstacle = Obstacle1(self)
                    self.obstacles.add(new_obstacle)

while True:
    game = Final()
    game.run_game()