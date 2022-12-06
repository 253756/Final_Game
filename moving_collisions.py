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

#points for second ship origin
f = 160
g = 600

#speed and starting points of obstacle
obstacle_speed = 3
obs_y = -30
speed = 1
obs_x = random.randint(0, 640)

#bring in health starting points
life_x = random.randint(0,640)
life_y = -60

obstacles = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    #movement of player 1
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    #set the boundaries for player 1
    if x >= 624:
        x = 624
    if x < 21:
       x = 20
    #movement of player 2 and boundaries
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

    #when life leaves the boundaries
    if life_y >= 640:
        life_y = -60
        life_x = random.randint(0,640)
        player1.health -= 50
        player2.health -= 50

    # obstacle move down the screen
    obs_y = obs_y + obstacle_speed

    #move health down the screen
    life_y = life_y + obstacle_speed

    #draw obstacle on screen
    obstacle = Obstacle1(screen, obs_x, obs_y)
    obstacle_rect = obstacle.rect

    def create_obstacle(num):
       for i in range(1,num+1):
        obstacle = Obstacle1(screen, obs_x, obs_y)
        obstacles.add(obstacle)
    create_obstacle(5)

    #draw life on screen
    life = Health(screen, life_x, life_y)

    #collision of obstacles and life with players
    collision1 = pygame.sprite.collide_rect(player1, obstacle)
    collision2 = pygame.sprite.collide_rect(player2,obstacle)
    collision3 = pygame.sprite.collide_rect(player1, life)
    collision4 = pygame.sprite.collide_rect(player2, life)
    #collision with obstacle -- loose health
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

    #collision with life -- gain health
    if collision3:
        player1.health += 10
        life_y = -60
        life_x = random.randint(0, 640)
    if collision4:
        player2.health += 10
        life_y = -60
        life_x = random.randint(0, 640)
    update()
    player1_rect = player1.rect

    #draw ships and obstacles to screen
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
