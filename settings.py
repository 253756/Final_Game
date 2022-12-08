import pygame

class Settings:
    def __init__(self):
        #calls the function
        self.speed()
        #controls numbers
        self.increase = 0.05
        self.life_speed = self.life_speed
        self.level = 0
        self.bg_color = (230,230,230)


    def speed(self):
        """initializes the speeds"""
        self.obstacle_speed = 2.5
        self.life_speed = 2.5

    def increase_speed(self):
        """changes speed"""
        self.life_speed += self.increase
        self.obstacle_speed += self.increase
