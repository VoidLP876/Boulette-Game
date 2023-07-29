import pygame
from pygame.locals import *
import time
import random
from Pong.paddle import *

def refresh():
    pygame.display.flip()
pygame.init()
fenetre = pygame.display.set_mode((1400,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()

paddles = [
    Paddle(700, 100, 100, 20, "Assets/paddlebleuv1.png"),
]
oldTime = pygame.time.get_ticks()
IsGameRunning = 1

paddle = pygame.image.load("Assets/paddlebleuv1.png")
paddle = pygame.transform.scale (paddle, (100,20))

fond = pygame.image.load("Assets/Nyan.PNG").convert()
fond = pygame.transform.scale(fond, (ScreenWidth,ScreenHeight))

pygame.mixer.music.load('Assets/music.mp3')
pygame.mixer.music.play(-1, 0.0)

pygame.display.flip()

while IsGameRunning:
    randomevent = random.randint (0,5000)
    if randomevent == 5000:
        randomeffect = 1
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

        
