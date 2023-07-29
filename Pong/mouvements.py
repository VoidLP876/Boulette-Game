import pygame
pygame.init()
ecran = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
pygame.display.set_caption("Fenêtre")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






pygame.quit()