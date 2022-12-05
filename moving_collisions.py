import pygame
import sys
from ship_1 import Ship1
from test_obstacle import Ship2
import random
from obstacle_1 import Obstacle1
from health import Health
pygame.init()

background_tile = pygame.image.load("images/water_tile.png")
water_rect = background_tile.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size,10*tile_size))
screen.fill((0,0,0))
screen_rect = screen.get_rect()
rows = screen_rect.height // tile_size
cols = screen_rect.width // tile_size


#drawing my ocean onthe screen
def update():
    for x in range(int(rows)):
        for y in range(int(cols)):
            screen.blit(background_tile, (x*water_rect.height, y*water_rect.width))

#bring in player 1
player1 = Ship1()

pygame.display.flip()
#points for the first ship origin
x = 320
y=600

clock = pygame.time.Clock()
obstacle_speed = 3
obs_y = -30
speed = 1
obs_x = random.randint(0, 640)

#bring in health
life = Health(screen)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    # set the boundaries
    if x >= 624:
        x = 624
        # need to fix this currerntly center is at the end
    if x < 21:
        x = 20
    if obs_y >= 640:
        obs_y = -30
        obs_x = random.randint(0,640)
        obstacle_speed = random.randint(2,5)
    obs_y = obs_y + obstacle_speed
    obstacle = Obstacle1(screen, obs_x, obs_y)
    obstacle2 = Obstacle1(screen, 0, 0)
    obstacle_rect = obstacle.rect
    collision = pygame.sprite.collide_rect(player1, obstacle)
    if collision:
        player1.health -= 50
        print("you just got hit")
        print(player1.health)
        obs_y = -30
        obs_x = random.randint(0, 640)
        obstacle_speed = random.randint(2, 5)
    update()
    player1_rect = player1.rect
    player1.draw(screen)
    obstacle.draw(screen)
    obstacle2.draw(screen)
    life.draw(screen)
    coordinate = (x,y)
    player1.move(coordinate)
    clock.tick(100)
    pygame.display.flip()
