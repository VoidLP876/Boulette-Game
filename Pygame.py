import pygame
from pygame.locals import *
import time
import random
test = random.randint(0,180) 
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((640,480), RESIZABLE)
w, h = pygame.display.get_surface().get_size()
windowsize = [w , h]
IsGameRunning = 1
fond = pygame.image.load("Nyan.PNG").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()
while IsGameRunning:
    w, h = pygame.display.get_surface().get_size()
    if w  != windowsize[0]& h != windowsize[1]:
        pygame.transform.scale(fond, (w, h))
        windowsize = [w, h]
    for event in pygame.event.get():
        if event.type == QUIT :
            IsGameRunning = 0