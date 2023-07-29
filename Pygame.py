import pygame
from pygame.locals import *
import time
import random
test = random.randint(0,180) 
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((1366,720), FULLSCREEN )
ScreenWidth, ScreenHeigh = fenetre.get_size()

oldTime = pygame.time.get_ticks()

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

    for event in pygame.event.get():
        if event.type == QUIT or event.key == pygame.K_ESCAPE: # ECHAP
            IsGameRunning = 0
        
