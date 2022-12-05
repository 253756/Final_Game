import pygame
import sys
from ship_1 import Ship1
import random
from obstacle_1 import Obstacle1
from health import Health
from ship_2 import Ship2

pygame.init()

background_tile = pygame.image.load("images/water_tile.png")
water_rect = background_tile.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size,10*tile_size))
screen.fill((0,0,0))
screen_rect = screen.get_rect()
rows = screen_rect.height // tile_size
cols = screen_rect.width // tile_size
clock = pygame.time.Clock()


#drawing my ocean on the screen
def update():
    for x in range(int(rows)):
        for y in range(int(cols)):
            screen.blit(background_tile, (x*water_rect.height, y*water_rect.width))

#bring in player 1
player1 = Ship1()

#bring in player 2
player2 = Ship2()

#points for the first ship origin
x = 480
y=600

f = 160
g = 600
obstacle_speed = 3
obs_y = -30
speed = 1
obs_x = random.randint(0, 640)

#bring in health
life_x = random.randint(0,640)
life_y = -30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    if x < 21:
        x = 20
    #movement of player 2
    if keys[pygame.K_a]:
        f -= 3
    if keys[pygame.K_d]:
        f += 3
    if f >= 624:
        f = 624
    if f < 21:
        f = 20

    #when obstacle leaves the boundaries
    if obs_y >= 640:
        obs_y = -30
        obs_x = random.randint(0,640)
        obstacle_speed = random.randint(2,5)
    if life_y >= 640:
        life_y = -30
        life_x = random.randint(0,640)
        player1.health -= 50
        player2.health -= 50

    # obstacle move down the screen
    obs_y = obs_y + obstacle_speed
    life_y = life_y + obstacle_speed
    obstacle = Obstacle1(screen, obs_x, obs_y)
    obstacle2 = Obstacle1(screen, 0, 0)
    obstacle_rect = obstacle.rect
    life = Health(screen, life_x, life_y)
    collision1 = pygame.sprite.collide_rect(player1, obstacle)
    collision2 = pygame.sprite.collide_rect(player2,obstacle)
    if collision1:
        player1.health -= 50
        print("you just got hit")
        print(player1.health)
        obs_y = -30
        obs_x = random.randint(0, 640)
        obstacle_speed = random.randint(2, 5)
    if collision2:
        player2.health -= 50
        print("you just got hit")
        print(player2.health)
        obs_y = -30
        obs_x = random.randint(0, 640)
        obstacle_speed = random.randint(2, 5)
    update()
    player1_rect = player1.rect
    player1.draw(screen)
    player2.draw(screen)
    obstacle.draw(screen)
    life.draw(screen)
    coordinate = (x,y)
    coordinate2 = (f,g)
    player2.move(coordinate2)
    player1.move(coordinate)
    clock.tick(100)
    pygame.display.flip()
