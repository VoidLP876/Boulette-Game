from math import sin, cos, tan, pow, sqrt, radians
from pygame import Vector2
class Ball:
    def __init__(self, screen, X, Y,dir,sprite):
        self.r = 0
        self.x = X
        self.y = Y
        self.Vx = cos(radians(dir)) *(sqrt(pow(screen.get_width(),2)-pow(screen.get_height(),2)))/self.speed
        self.Vy = sin(radians(dir)) *(sqrt(pow(screen.get_width(),2)-pow(screen.get_height(),2)))/self.speed
        self.dir = dir
        self.sprite = sprite
        self.speed = 60
    def ChangeTarget(self, screen):
       self.Vx = cos(radians(self.dir)) *(sqrt(pow(screen.get_width(),2)-pow(screen.get_height(),2)))/self.speed
       self.Vy = sin(radians(self.dir)) *(sqrt(pow(screen.get_width(),2)-pow(screen.get_height(),2)))/self.speed
    def MoveBall(self):
        self.x += self.Vx
        self.y += self.Vy