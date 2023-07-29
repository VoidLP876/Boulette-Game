import pygame
from pygame.locals import *
import time
import random
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((1366,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()
IsGameRunning = 1

fond = pygame.image.load("Assets/Nyan.PNG").convert()
fond = pygame.transform.scale(fond, (ScreenWidth,ScreenHeight))

fenetre.blit(fond, (0,0))
pygame.mixer.music.load('Assets/music.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.display.flip()
while IsGameRunning:
    # deltatime
    t = pygame.time.get_ticks()
    deltaTime = (t - oldTime) / 1000.0
    oldTime = t

    for event in pygame.event.get():
        if event.type == QUIT : # ECHAP
            IsGameRunning = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                IsGameRunning = 0

        
