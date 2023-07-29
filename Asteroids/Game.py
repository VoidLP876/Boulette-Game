import pygame
import time
import random
from projectile import *
import player 
from EnemyManager import *
from time import sleep
from math import sin, cos, pi, radians, atan2, sqrt, pow
from sys import exit 
from Upgardes import *

bullets = []
Upgrades = []

dt = 0
r = 90
timelock = 1
stroidsTime = time.time() + 1
cooldown = .3
AsteroidsCooldown = 1.5
Score = 0

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True
Play = player.Player(screen.get_width() / 2, screen.get_height() / 2)

pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(Play.Score), True, "white")

def Colision(b):
    for stroid in asteroids:
        if abs(b.PosX - stroid.PosX) <= 20 and abs(b.PosY - stroid.PosY) <= 20:
            asteroids.pop(asteroids.index(stroid))
            Play.Score += 1
            bullets.remove(b)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if Play.Life <= 0:
        running = False
    screen.fill("black")
    Play.PlayerMovement( screen)
    Play.Input()
    MoveEnemies(Play, screen)
    DrawEnemies(screen)
    textRect = text.get_rect()
    textRect.center = (screen.get_width() / 2, screen.get_height() / 2)
    text = font.render(str(Play.Score), True, "white")
    screen.blit(text, textRect)
    triangle1 = player.makeTriangle(20, 1, r)
    player.offsetTriangle(triangle1, Play.x, Play.y)
    player.drawTriangle(triangle1, screen)
    for bullet in bullets:
        if bullet.PosX < screen.get_width() and bullet.PosX > 0 and  bullet.PosY < screen.get_height() and bullet.PosY > 0:
            bullet.Move()
            Colision(bullet)
            bullet.draw(screen)
        else:    
            bullets.pop(bullets.index(bullet))
    if time.time() >= stroidsTime:
        AsteroidsManager(screen)   
        if AsteroidsCooldown >= .4:
            AsteroidsCooldown-= random.uniform(0.002, 0.005)
        stroidsTime += AsteroidsCooldown
    pygame.display.flip()
    if pygame.mouse.get_pressed()[0] and time.time() >= timelock:
        bulletVelX = cos(radians(r+90)) *(sqrt(pow(screen.get_width(),2)-pow(screen.get_height(),2)))/70
        bulletVelY = sin(radians(r+90)) *(sqrt(pow(screen.get_width(),2)-pow(screen.get_height(),2)))/70
        projectile = Projectile(bulletVelX, bulletVelY, Play.x, Play.y)
        bullets.append(projectile)
        timelock = time.time()+cooldown
    mousePosX, mousePosY = pygame.mouse.get_pos()
    diffX = mousePosX - Play.x
    diffY = mousePosY - Play.y
    r = atan2(diffY,diffX)* (180 / pi) - 90
    clock.tick(60)
    dt = clock.tick(60) / 1000
pygame.quit()
