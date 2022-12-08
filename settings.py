import pygame

class Settings:
    def __init__(self):
        self.speed()
        self.increase = 0.05
        self.life_speed = self.life_speed
        self.level = 1
        self.bg_color = (230,230,230)


    def speed(self):
        self.obstacle_speed = 2.5
        self.life_speed = 2.5

    def increase_speed(self):
        self.life_speed += self.increase
        self.obstacle_speed += self.increase
