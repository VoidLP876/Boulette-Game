import pygame
from pygame.locals import *
import time
import random
def refresh():
    pygame.display.flip()
    fenetre.blit(fond, (0,0))       #ICI
    fenetre.blit(paddle, (xpos,250))  #ICI
pygame.init()
fenetre = pygame.display.set_mode((1366,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()
IsGameRunning = 1

paddle = pygame.image.load("Assets/paddlebleuv1.png")
paddle = pygame.transform.scale (paddle, (100,20))

fond = pygame.image.load("Assets/Nyan.PNG").convert()
fond = pygame.transform.scale(fond, (ScreenWidth,ScreenHeight))

xpos = 500

fenetre.blit(fond, (0,0))
fenetre.blit(paddle, (xpos,250))

pygame.mixer.music.load('Assets/music.mp3')
pygame.mixer.music.play(-1, 0.0)

pygame.display.flip()

oldTime = 0

while IsGameRunning:
    randomevent = random.randint (0,5000)
    if randomevent == 5000:
        randomeffect = 1
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
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        if xpos >= 340:
            xpos -= 1  
            time.sleep(0.002)
            refresh()
    if keys_pressed[pygame.K_RIGHT]:
        if xpos + 100 <= 1060:
            xpos += 1
            time.sleep(0.002)
            refresh()
    

        
