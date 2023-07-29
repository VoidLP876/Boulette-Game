import pygame
from pygame.locals import *
import time
import random
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((1366,720), FULLSCREEN )
ScreenWidth, ScreenHeigh = fenetre.get_size()

oldTime = pygame.time.get_ticks()

class Particle():
    def __init__(self, startx, starty, col):
        self.x = startx
        self.y = random.randint(0, starty)
        self.col = col
        self.sx = startx
        self.sy = starty

    def move(self):
        if self.y < 0:
            self.x=self.sx
            self.y=self.sy

        else:
            self.y-=1

        self.x+=random.randint(-2, 2)

IsGameRunning = 1
fond = pygame.image.load("Assets/Nyan.PNG").convert()
fond = pygame.transform.scale(fond, (1366, 768))
fenetre.blit(fond, (0,0))
pygame.display.flip()
while IsGameRunning:
    # deltatime
    t = pygame.time.get_ticks()
    deltaTime = (t - oldTime) / 1000.0
    oldTime = t

    particles = []
    for part in range(300):
        if part % 2 > 0: col = black
        else: col = grey
        particles.append( Particle(515, 500, col) )
    for p in particles:
            p.move()
            pygame.draw.circle(fenetre, p.col, (p.x, p.y), 2)
            refresh()
    for event in pygame.event.get():
        if event.type == QUIT : # ECHAP
            IsGameRunning = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                IsGameRunning = 0
        
