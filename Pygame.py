import pygame
from pygame.locals import *
from Pong.Ball import *
from Pong.paddle import Paddle
import time

pygame.init()
fenetre = pygame.display.set_mode((1400,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()

ball = Ball(700, 360, 500)
paddles = [
    Paddle(650, 50, 100, 20, "Assets/paddlebleuv1.png"),
    Paddle(390, 310, 20, 100, "Assets/paddlejaunev1.png"),
    Paddle(650, 650, 100, 20, "Assets/paddlerougev1.png"),
    Paddle(990, 310, 20, 100, "Assets/paddlevertv1.png"),
]


oldTime = pygame.time.get_ticks()
IsGameRunning = 2
accueil = pygame.image.load("Assets/backgroundv3.png").convert()
accueil = pygame.transform.scale(accueil, (ScreenWidth,ScreenHeight))
playbutton = pygame.image.load("Assets/Play.png").convert_alpha()
fond = pygame.image.load("Assets/backgroundv1.png").convert()
fond = pygame.transform.scale(fond, (ScreenWidth,ScreenHeight))
surcouche = pygame.image.load("Assets/backgroundcarrev1.png").convert()
fenetre.blit(fond, (0,0))

music1 =pygame.mixer.Sound('Assets/music.mp3')

music1.play()
pygame.display.flip()

def refresh():
    fenetre.blit(fond, (0,0))
    fenetre.blit(surcouche, (340,0))
    for paddle in paddles:
        paddle.draw(fenetre)
    ball.Draw(fenetre)

while IsGameRunning > 0:
    if IsGameRunning == 2:
        fenetre.blit(accueil, (0,0))
        fenetre.blit(playbutton,(650, 360))

        mousex, mousey = pygame.mouse.get_pos()
        bouton_souris = pygame.mouse.get_pressed()
        if bouton_souris[0]:
            if 650 <= mousex <= 800 and 360 <= mousey <= 400:
                IsGameRunning = 1

        pygame.display.flip()
        for event in pygame.event.get():
            #LEAVE GAME
            if event.type == QUIT :
                IsGameRunning = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    IsGameRunning = 0
                    pygame.quit()
    
    if IsGameRunning == 1:
        # deltatime
        t = pygame.time.get_ticks()
        deltaTime = (t - oldTime) / 1000.0
        oldTime = t

        ball.CollidePaddles(paddles)
        dead = ball.MoveBall(deltaTime)
        if dead > -1:
            paddles[dead].isAlive = False

        keys_pressed = pygame.key.get_pressed()

        #J1 BLEU
        if keys_pressed[pygame.K_w]:
            paddles[0].move(deltaTime, -1, 0)
            if(paddles[0].isTouchingWallX()):
                paddles[0].move(deltaTime, 1, 0)
        if keys_pressed[pygame.K_x]:
            paddles[0].move(deltaTime, 1, 0)
            if(paddles[0].isTouchingWallX()):
                paddles[0].move(deltaTime, -1, 0)

        #J2 JAUNE
        if keys_pressed[pygame.K_a]:
            paddles[1].move(deltaTime, -1, 1)
            if(paddles[1].isTouchingWallY()):
                paddles[1].move(deltaTime, 1, 1)
        if keys_pressed[pygame.K_q]:
            paddles[1].move(deltaTime, 1, 1)
            if(paddles[1].isTouchingWallY()):
                paddles[1].move(deltaTime, -1, 1)

        #J3 ROUGE
        if keys_pressed[pygame.K_LEFT]:
            paddles[2].move(deltaTime, -1, 0)
            if(paddles[2].isTouchingWallX()):
                paddles[2].move(deltaTime, 1, 0)
        if keys_pressed[pygame.K_DOWN]:
            paddles[2].move(deltaTime, 1, 0)
            if(paddles[2].isTouchingWallX()):
                paddles[2].move(deltaTime, -1, 0)

        #J4 VERT
        if keys_pressed[pygame.K_KP9]:
            paddles[3].move(deltaTime, -1, 1)
            if(paddles[3].isTouchingWallY()):
                paddles[3].move(deltaTime, 1, 1)
        if keys_pressed[pygame.K_KP6]:
            paddles[3].move(deltaTime, 1, 1)
            if(paddles[3].isTouchingWallY()):
                paddles[3].move(deltaTime, -1, 1)

            #LEAVE GAME
        for event in pygame.event.get():
            if event.type == QUIT :
                IsGameRunning = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    IsGameRunning = 0
                    pygame.quit()


        refresh()

        pygame.display.flip()