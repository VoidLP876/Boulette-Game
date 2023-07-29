import pygame
class Upgrade:
    def __init__(self, x, y, Upgrade ):
        self.x = x
        self.y = y
        self.UpGrade = Upgrade
    def draw(self, screen):
        pygame.draw.polygon(screen, "white",((self.x+.5,self+.5),(self.x-.5,self+.5 ),(self.x-.5,self-.5 ),(self.x+.5,self-.5 )))