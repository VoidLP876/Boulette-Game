from math import sin, cos, pow, sqrt, radians
import pygame
class Ball:
    def __init__(self, X, Y,dir):#sprite):
        self.r = 0
        self.x = X
        self.y = Y
        self.speed = 750
        self.Vx = cos(radians(dir)) *(sqrt(pow(720,2)+pow(720,2)))/self.speed
        self.Vy = sin(radians(dir)) *(sqrt(pow(720,2)+pow(720,2)))/self.speed
        self.dir = dir
        #self.sprite = sprite
    def Draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 5)
    def MoveBall(self):
        self.x += self.Vx
        self.y += self.Vy
        if self.x > 1060 or self.x < 340:
            self.Vx *= -1
        if self.y > 1060 and self.y < 340:
            self.Vy *= -1
        