import pygame
import sys

class Ship1:
    def __init__(self):
        self.image = pygame.image.load("images/ship1.png")
        self.dead_image = pygame.image.load('images/dead_ship.png')
        self.rect = self.image.get_rect()
        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.health = 1000


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
            print("no")
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
            print('n')

    def _check_keyup_events(self,event):
        """"Respond to key realeases."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
            print("yes")
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
            print("y")
        elif event.key == pygame.K_q:
            sys.exit()

   # def update(self):
    #    """Update the ship's position based on teh movement flag"""
     #   # Update the ship's x value, not the rect.
      #  if self.moving_right and self.rect.right < self.screen_rect.right:
       #     self.x += self.settings.ship_speed
       # if self.moving_left and self.rect.left > 0:
        #    self.x -= self.settings.ship_speed

        # update rect object from self.x.
      #  self.rect.x = self.x
    def draw(self, surface):
        if self.health <=300:
            self.image = self.image
        if self.health <= 0:
            self.image = self.dead_image
        surface.blit(self.image, self.rect)

    def move(self, coordinate):
        self.rect.center = coordinate