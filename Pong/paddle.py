import pygame

class Paddle:
    def __init__(self, x, y, w, h, spritePath):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sprite = pygame.image.load(spritePath).convert()
        self.sprite = pygame.transform.scale(self.sprite, (w, h))
    
    def move(self, mx, my, dt):
        self.x += mx * dt
        self.y += my * dt
    
    def draw(self, window):
        window.blit(self.sprite, (self.x, self.y))