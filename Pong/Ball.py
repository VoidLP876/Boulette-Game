from math import sin, cos, tan, pow
from pygame import Vector2
class Ball:
    def __init__(self, screen, X, Y,Vy, Vx, dir, sprite):
        self.r = 0
        self.x = X
        self.y = Y
        self.dir = dir
        self.Vx = Vx
        self.Vy = Vy
        d = screen.get_width() pow(screen.get_height()-self.y,2)
        self.sprite = sprite
        self.Target = Vector2(d)