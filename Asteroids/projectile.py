import pygame
#from Game import bullets
class Projectile:
    def __init__(self, vX, vY, PosX, PosY):
        self.vX = vX
        self.vY = vY
        self.PosX = PosX
        self.PosY = PosY
    def Move(self):
        self.PosX += self.vX
        self.PosY += self.vY
    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.PosX,self.PosY), 2)
    