import pygame
from pygame.locals import *
import time
import random
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((1400, 720), FULLSCREEN )
ScreenWidth, ScreenHeigh = fenetre.get_size()
IsGameRunning = 1
fond = pygame.image.load("Assets/Nyan.PNG").convert()
fond = pygame.transform.scale(fond, (ScreenWidth,ScreenHeight))

fenetre.blit(fond, (0,0))
pygame.mixer.music.load('Assets/music.mp3')

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
<<<<<<< HEAD
=======
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        if xpos >= 340:
            xpos -= 1  
            time.sleep(0.002)
    if keys_pressed[pygame.K_RIGHT]:
        if xpos + 100 <= 1060:
            xpos += 1
            time.sleep(0.002)
    
>>>>>>> a9ce60bd58e90a91ac6a76efe96c7f1fce0dc324

        
