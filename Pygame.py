import pygame
from pygame.locals import *
import time
import random
test = random.randint(0,180) 
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode(FULLSCREEN)
IsGameRunning = 1
fond = pygame.image.load("Nyan.PNG").convert()
pygame.transform.scale(fond, (1366, 720))
fenetre.blit(fond, (0,0))
pygame.display.flip()
while IsGameRunning:
        windowsize = [w, h]
    for event in pygame.event.get():
        if event.type == QUIT :
            IsGameRunning = 0