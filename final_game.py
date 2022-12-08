import pygame
import sys
from ship_1 import Ship1
from obstacle_1 import Obstacle1
from health import Health
from ship_2 import Ship2
from buttons import Button
from settings import Settings
from score import Score

class Final():
    def __init__(self):
        pygame.init()
        #create screen background
        self.background_tile = pygame.image.load("images/water_tile.png")
        self.water_rect = self.background_tile.get_rect()
        self.tile_size = self.water_rect.width
        self.screen = pygame.display.set_mode((10*self.tile_size,10*self.tile_size))
        self.color = (0,0,0)
        self.screen.fill((self.color))
        self.screen_rect = self.screen.get_rect()
        self.rows = self.screen_rect.height//self.tile_size
        self.cols = self.screen_rect.width//self.tile_size

        self.settings = Settings()

        #bring in players
        self.player1 = Ship1(self)
        self.player2 = Ship2(self)

        #draw in from files
        self.clock = pygame.time.Clock()
        self.obstacles = pygame.sprite.Group()
        self.lifes = pygame.sprite.Group()
        self.button = Button(self)
        self.score = Score(self)

        #initialize for button
        self.active = False

    def run_game(self):
        #helped with button - Ethan
        #call function with blank screen and button
        self.first_screen()
        while True:
            #call movements
            self._check_events()
            #when button is clicked active becomes True
            if self.active == True:
                self.update()
                self.player1.updates()
                self.player2.updates()
                self._drop_obstacles()
                self._check_obstacles_bottom()
                self.obstacles.update()
                self._drop_lifes()
                self._check_lifes_bottom()
                self.lifes.update()
                self._update_obstacles()
                self._update_lifes()
                self.check_health()
                self.clock.tick(100)

    def first_screen(self):
        """Screen for button with multiple screen"""
        self.screen.fill((0,0,0))
        if not self.active:
            self.button.draw_button()
        pygame.display.flip()

    def update(self):
        """Drawing screen with tiles and ojects"""
        for x in range(int(self.rows)):
            for y in range(int(self.cols)):
                self.screen.blit(self.background_tile, (x*self.water_rect.height, y*self.water_rect.width))
        self.player1.blitme()
        self.player2.blitme()
        for obstacle in self.obstacles.sprites():
            obstacle.draw()
        for life in self.lifes.sprites():
            life.draw()
        self.score.show()
        pygame.display.flip()

    def _check_events(self):
        """Movement of players"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    def _check_button(self, mouse_pos):
        """When button is clicked active is True and loop starts working"""
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.active:
            self.active = True

    def _keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.player1.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player1.moving_left = True
        elif event.key == pygame.K_d:
            self.player2.moving_right = True
        elif event.key == pygame.K_a:
            self.player2.moving_left = True
    def _keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.player1.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player1.moving_left = False
        elif event.key == pygame.K_d:
            self.player2.moving_right = False
        elif event.key == pygame.K_a:
            self.player2.moving_left = False
    def _player1_and_obstacle_collision(self):
        """When player1 and obstacle collide the health goes down and score changes"""
        collisions = pygame.sprite.spritecollide(self.player1, self.obstacles, True)
        if collisions:
            # If collision detected add a point
            self.player1.health -= 100
            self.score.player1_score()

    def _player2_and_obstacle_collision(self):
        """When player2 and obstacle collide the health goes down and score changes"""
        collisions = pygame.sprite.spritecollide(self.player2, self.obstacles, True)
        if collisions:
            # If collision detected add a point
            self.player2.health -= 100
            self.score.player2_score()

    def _check_obstacles_bottom(self):
        '''It checks if the obstacle crosses the screen bottom'''
        screen_rect = self.screen.get_rect()
        for obstacle in self.obstacles.sprites():
            if obstacle.rect.bottom >= screen_rect.bottom:
                break

    def _drop_obstacles(self):
        '''Drop obstacles from the top, randomly'''
        if len(self.obstacles) == 0:
                new_obstacle = Obstacle1(self)
                self.obstacles.add(new_obstacle)
        if len(self.obstacles) == 1:
            for obstacle in self.obstacles.sprites():
                #print(obstacle.rect)
                if obstacle.rect.bottom > 200:
                    new_obstacle = Obstacle1(self)
                    self.obstacles.add(new_obstacle)
        if len(self.obstacles) == 2:
            for obstacle in self.obstacles.sprites():
                if obstacle.rect.bottom > 400:
                    new_obstacle = Obstacle1(self)
                    self.obstacles.add(new_obstacle)
        if len(self.obstacles) == 3:
            for obstacle in self.obstacles.sprites():
                if obstacle.rect.bottom > 600:
                    new_obstacle = Obstacle1(self)
                    self.obstacles.add(new_obstacle)

    def _update_obstacles(self):
        '''If a obstacle crosses the window, it disappears'''
        for obstacle in self.obstacles.copy():
            if obstacle.rect.bottom >= self.screen_rect.bottom:
                self.obstacles.remove(obstacle)
        self._player1_and_obstacle_collision()
        self._player2_and_obstacle_collision()

    def _check_lifes_bottom(self):
        '''It checks if the life crosses the screen bottom'''
        screen_rect = self.screen.get_rect()
        for life in self.lifes.sprites():
            if life.rect.bottom >= screen_rect.bottom:
                break

    def _drop_lifes(self):
        '''Drop life from the top, randomly'''
        if len(self.lifes) == 0:
            new_life = Health(self)
            self.lifes.add(new_life)
        if len(self.lifes) == 1:
            for life in self.lifes.sprites():
                #print(life.rect)
                if life.rect.bottom > 300:
                    new_life = Health(self)
                    self.lifes.add(new_life)
        if len(self.lifes) == 2:
            for life in self.lifes.sprites():
                if life.rect.bottom > 500:
                    new_life = Health(self)
                    self.lifes.add(new_life)
        if len(self.lifes) == 3:
            for life in self.lifes.sprites():
                if life.rect.bottom > 700:
                    new_life = Health(self)
                    self.lifes.add(new_life)


    def _update_lifes(self):
        """removes life if it crosses the window"""
        for life in self.lifes.copy():
            if life.rect.bottom >= self.screen_rect.bottom:
                self.lifes.remove(life)
        self.life_and_player1()
        self.life_and_player2()
    def life_and_player1(self):
        """When player1 and life collide the health goes up and score changes"""
        collisions = pygame.sprite.spritecollide(self.player1, self.lifes, True)
        if collisions:
            # If collision detected add a point
            self.player1.health += 10
            self.score.player1_score()
            self.level_up()

    def life_and_player2(self):
        """When player2 and life collide the health goes up and score changes"""
        collisions = pygame.sprite.spritecollide(self.player2, self.lifes, True)
        if collisions:
            # If collision detected add a point
            self.player2.health +=10
            self.score.player2_score()
            self.level_up()

    def level_up(self):
        """speed increases as level increases
        level changes and updates on the screen"""
        self.settings.increase_speed()
        if self.settings.life_speed and self.settings.obstacle_speed >= 6:
            self.settings.life_speed = 6
            self.settings.obstacle_speed = 6
        if self.settings.life_speed >= 3:
            self.settings.level = 2
        elif self.settings.life_speed >= 4:
            self.settings.level = 3
        elif self.settings.life_speed >= 5:
            self.settings.level = 4
        elif self.settings.life_speed >= 6:
            self.settings.level = 5
        self.score.prep_level()

    def check_health(self):
        """"when health is below 50 the game quits and is done"""
        if self.player1.health <= -50:
            pygame.quit()
            sys.exit()
        if self.player2.health <= -50:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    game = Final()
    game.run_game()