import pygame

class Paddle:
    def __init__(self, x, y, w, h, spritePath):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sprite = pygame.image.load("Assets/Nyan.PNG").convert()
        self.sprite = pygame.transform.scale(self.sprite, (1400, 720))
    
    def move(self, mx, my, dt):
        self.x += mx * dt
        self.y += my * dt
    