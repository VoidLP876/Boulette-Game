from time import sleep
from asteroid import *
asteroids = []

def AsteroidsManager(screen):
    asteroid = Asteroid(screen)
    asteroids.append(asteroid)

def MoveEnemies(player, screen):
    for stroids in asteroids:
        if stroids.PosX < screen.get_width()+21 and stroids.PosX > -21 and  stroids.PosY < screen.get_height()+21 and stroids.PosY > -21:
            stroids.PosX += stroids.vX
            stroids.PosY += stroids.vY
            if abs(player.x - stroids.PosX) <= 20 and abs(player.y - stroids.PosY) <= 20:
                player.Life -= 1
            #offsetHexagon(stroids.Hex, stroids.PosX, stroids.PosY)
        else:
            asteroids.remove(stroids)
            
def DrawEnemies(screen):
    for stroid in asteroids:
        stroid.draw(screen)
