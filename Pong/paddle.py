import pygame

class Paddle:
    def __init__(self, x, y, w, h, spritePath):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sprite = pygame.image.load(spritePath).convert()
        self.sprite = pygame.transform.scale(self.sprite, (w, h))

    def move(self, dt, direction, isRotated):
        self.x += (direction * isRotated * 100) * dt 
        self.y += (direction * (not isRotated) * 100) * dt 
    
    def draw(self, window):
        window.blit(self.sprite, (self.x, self.y))
    
    def isTouchingWallX(self):
        return self.x < 340 or self.x + self.width >= 1060

    def isTouchingWallY(self):
        return self.y < 0 or self.y + self.h >= 720