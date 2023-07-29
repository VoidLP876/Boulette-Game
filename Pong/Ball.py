from math import sin, cos, pow, sqrt, radians
import pygame
from paddle import Paddle

class Ball:
    def __init__(self, X, Y, speed):#sprite):
        self.r = 0
        self.x = X
        self.y = Y
        self.Vx = 0
        self.Vy = speed
        #self.sprite = sprite
    def Draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 5)
    def MoveBall(self, dt):
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        if self.x > 1060 or self.x < 340:
            self.Vx *= -1
        if self.y > 800 or self.y < 0:
            self.Vy *= -1
    def CollidePaddles(self, paddles):
        for i, paddle in enumerate(paddles):
            if paddle.x > self.x and self.x <= paddle.x + paddle.width and paddle.y > self.y and self.y <= paddle.y + paddle.height:
                
