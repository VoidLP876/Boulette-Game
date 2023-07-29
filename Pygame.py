import pygame
from pygame.locals import *
import time
import random
from Pong.paddle import *

def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((1400,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()

paddles = [
    Paddle(100, 100, 100, 20, "Assets/paddlebleuv1.png"),
]
oldTime = pygame.time.get_ticks()
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

        
