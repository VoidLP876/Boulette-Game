from Ball import *
import pygame

pygame.init()
screen = pygame.display.set_mode((1400, 720))
clock = pygame.time.Clock()
screen.fill("black")
running = True
ball = Ball(700, 360, 179)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball.MoveBall()
    ball.Draw(screen)
    pygame.display.flip()
    clock = pygame.time.Clock()
pygame.quit()