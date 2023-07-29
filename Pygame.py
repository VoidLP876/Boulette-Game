import pygame
from pygame.locals import *
import time
import random
test = random.randint(0,180) 
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((640,480), RESIZABLE)
IsGameRunning = 1
fond = pygame.image.load("Nyan.PNG").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()
while IsGameRunning:
    for event in pygame.event.get():
        if event.type == QUIT :
            IsGameRunning = 0
# moi aussi !