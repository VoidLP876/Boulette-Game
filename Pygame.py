import pygame
from pygame.locals import *
import time
import random
test = random.randint(0,180) 

pygame.init()
fenetre = pygame.display.set_mode((640,480), RESIZABLE)
IsGameRunning = 1
fond = pygame.image.load("Nyan.PNG").convert()
fenetre.blit(fond, (0,0))
while True: 
    print (test)