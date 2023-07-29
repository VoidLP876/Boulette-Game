import pygame
from pygame.locals import *
import time
import random
def refresh():
    pygame.display.flip
pygame.init()
fenetre = pygame.display.set_mode((1400,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()

paddles = [
    Paddle(700, 100, 100, 20, "Assets/paddlebleuv1.png"),
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

    fenetre.blit(fond, (0,0))

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        paddle.move(deltaTime, -1, 0)
        if(paddle.isTouchingWallX()):
            paddle.move(deltaTime, 1, 0)
    if keys_pressed[pygame.K_RIGHT]:
        paddle.move(deltaTime, 1, 0)
        if(paddle.isTouchingWallX()):
            paddle.move(deltaTime, -1, 0)
    
    for paddle in paddles:
        paddle.draw(fenetre)

    for event in pygame.event.get():
        if event.type == QUIT : # ECHAP
            IsGameRunning = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                IsGameRunning = 0

    refresh()

        
