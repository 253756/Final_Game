import pygame
import sys
from ship_1 import Ship1
from test_obstacle import Ship2
import random
from obstacle_1 import Obstacle1

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
x=50
y=520

clock = pygame.time.Clock()
obstacle = Obstacle1(screen, 0,0)

obstacle_width = obstacle.rect.width
available_space_x = 640 - (2*obstacle_width)
number_obstacles_x = available_space_x // (2*obstacle_width)

obstacle_height = obstacle.rect.height
available_space_y = 300 - (2*obstacle_height)
number_obstacles_y = available_space_y // (2*obstacle_height)
obstacles = pygame.sprite.Group()

for i in range(number_obstacles_x):
    for j in range(number_obstacles_y):
        obstacles.add(Obstacle1(screen, obstacle_width + 2 * obstacle_width * i, obstacle_height + 2 * obstacle_height * j))
#first obstacle
##obstacle = Ship2()
#position_y = 0
#position_x = random.randint(0,600)

#obstacle
#clock = pygame.time.Clock()
speed = 1
#obs_list = []

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=3
    elif keys[pygame.K_RIGHT]:
        x+=3
    #position_y += 1
    update()
    player1_rect = player1.rect
    #player1.draw(screen)
    screen.blit(player1.image, (x,y))
    obstacles.update()
    obstacles.draw(screen)
    pygame.display.flip()
    clock.tick(500)
    collision = pygame.sprite.collide_rect(player1,obstacle)
    if collision:
        player1.health -= 40
        print("you just got hit")
        print(player1.health)
    print(screen_rect)
    pygame.display.flip()
