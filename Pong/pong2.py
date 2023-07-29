import pygame
pygame.init()
largeur, hauteur = 850, 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Fenêtre")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






pygame.quit()