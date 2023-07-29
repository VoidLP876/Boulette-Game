import pygame
pygame.init()
largeur, hauteur = 500, 500
ecran = pygame.display.set_mode(((640,480), pygame.FULLSCREEN)
pygame.display.set_caption("Fenêtre")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






pygame.quit()