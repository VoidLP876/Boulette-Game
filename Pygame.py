import pygame
from pygame.locals import *
from Pong.Ball import *
from Pong.paddle import Paddle

pygame.init()
fenetre = pygame.display.set_mode((1400,720), FULLSCREEN )
ScreenWidth, ScreenHeight = fenetre.get_size()

ball = Ball(700, 360, 600)

paddles = [
    Paddle(700, 100, 100, 20, "Assets/paddlebleuv1.png"),
    Paddle(700, 100, 20, 100, "Assets/paddlebleuv1.png"),
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


while IsGameRunning == 1:
    # deltatime
    t = pygame.time.get_ticks()
    deltaTime = (t - oldTime) / 1000.0
    oldTime = t

    ball.MoveBall(deltaTime)

    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_LEFT]:
        paddles[0].move(deltaTime, -1, 0)
        if(paddles[0].isTouchingWallX()):
            paddles[0].move(deltaTime, 1, 0)
    if keys_pressed[pygame.K_RIGHT]:
        paddles[0].move(deltaTime, 1, 0)
        if(paddles[0].isTouchingWallX()):
            paddles[0].move(deltaTime, -1, 0)


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