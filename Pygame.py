import pygame
from pygame.locals import *
import time
import random
from Pong.paddle import Paddle

pygame.init()
fenetre = pygame.display.set_mode((1400,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()

paddles = [
    Paddle(700, 100, 100, 20, "Assets/paddlebleuv1.png"),
]
oldTime = pygame.time.get_ticks()
IsGameRunning = 2
accueil = pygame.image.load("Assets/Nyan.png").convert()
accueil = pygame.transform.scale(accueil, (ScreenWidth,ScreenHeight))
playbutton = pygame.image.load("Assets/Play.png")
fond = pygame.image.load("Assets/backgroundv1.png").convert()
fond = pygame.transform.scale(fond, (ScreenWidth,ScreenHeight))
surcouche = pygame.image.load("Assets/backgroundcarrev1.png").convert()
fenetre.blit(fond, (0,0))
pygame.mixer.music.load('Assets/music.mp3')

pygame.display.flip()

def refresh():
    pygame.display.flip()

    fenetre.blit(fond, (0,0))
    fenetre.blit(surcouche, (340,0))
    for paddle in paddles:
        paddle.draw(fenetre)
while IsGameRunning == 2:
    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE :
                IsGameRunning = 1
while IsGameRunning == 1:
    
    # deltatime
    t = pygame.time.get_ticks()
    deltaTime = (t - oldTime) / 1000.0
    oldTime = t

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        paddles[0].move(deltaTime, -1, 0)
        if(paddles[0].isTouchingWallX()):
            paddles[0].move(deltaTime, 1, 0)
    if keys_pressed[pygame.K_RIGHT]:
        paddles[0].move(deltaTime, 1, 0)
        if(paddles[0].isTouchingWallX()):
            paddles[0].move(deltaTime, -1, 0)

    for event in pygame.event.get():
        if event.type == QUIT : # ECHAP
            IsGameRunning = 0
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                IsGameRunning = 0
                pygame.quit()

    refresh()

        
