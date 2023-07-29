import pygame
import random
from math import sqrt, cos, sin, radians, acos, pow
def GeneratePos(screen, blacklist):
    side = random.randint(1,4)
    if side == blacklist:
        return GeneratePos(screen, blacklist)
    o = 20
    PosX, PosY = (0,0)
    match side:
        case 1:
            PosX = screen.get_width()+o
            PosY = random.randint(0, screen.get_height())
        case 2:
            PosX = -o
            PosY = random.randint(0, screen.get_height())
        case 3:
            PosX = random.randint(0, screen.get_width())
            PosY = screen.get_height()+o
        case 4:
            PosX = random.randint(0, screen.get_width())
            PosY = -o         
    return PosX, PosY, side

class Asteroid:
    def __init__(self, screen):
        self.vX = 0
        self.vY = 0
        self.PosX = 0
        self.PosY = 0
        self.TargetX = 0
        self.TargetY = 0
        self.rotation = 1
        self.Hex = MakeHexagon(20, self.rotation)
        self.Generate(screen)

    def Generate(self, screen):
        posX, posY, blacklist = GeneratePos(screen, 5)
        self.PosX = posX
        self.PosY = posY
        targetX, targetY, blacklist = GeneratePos(screen, blacklist)
        self.TargetX = targetX
        self.TargetY = targetY  
        dX = targetX-posX
        dY = targetY-posY
        speed = random.randint(47, 70)
        angle = acos(sqrt(pow(dX,2)+pow(dY, 2))/dY)
        self.vX = cos(angle)*sqrt(pow(dX,2)+pow(dY, 2))/speed
        self.vY = sin(angle)*sqrt(pow(dX,2)+pow(dY, 2))/speed

    def draw(self, screen, color=(255,255,255)):
        pygame.draw.circle(screen, color, (self.PosX, self.PosY), 20)
    def show(self, screen, color=(255,255,255)):
        Hex = self.Hex
        pygame.draw.line(screen, color, Hex.p1, Hex.p2)
        pygame.draw.line(screen, color, Hex.p2, Hex.p3)
        pygame.draw.line(screen, color, Hex.p3, Hex.p4)
        pygame.draw.line(screen, color, Hex.p4, Hex.p5)
        pygame.draw.line(screen, color, Hex.p5, Hex.p6)
        pygame.draw.line(screen, color, Hex.p6, Hex.p1)
class Hexagon:
    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6

def MakeHexagon(scale, rotation):
    p1 = ( 1, 0 ) 
    p2 = ( 0.5, sqrt(3/2))
    p3 = (-0.5, sqrt(3/2)) 
    p4 = (-1, 0 ) 
    p5 = (-0.5, -sqrt(3/2))
    p6 = ( 0.5, -sqrt(3/2))
    ra = radians(rotation)
    rp1x = p1[0] * cos(ra) - p1[1] * sin(ra)
    rp1y = p1[0] * sin(ra) + p1[1] * cos(ra)                 
    rp2x = p2[0] * cos(ra) - p2[1] * sin(ra)
    rp2y = p2[0] * sin(ra) + p2[1] * cos(ra)                        
    rp3x = p3[0] * cos(ra) - p3[1] * sin(ra)                         
    rp3y = p3[0] * sin(ra) + p3[1] * cos(ra)
    rp4x = p4[0] * cos(ra) - p4[1] * sin(ra)
    rp4y = p4[0] * sin(ra) + p4[1] * cos(ra)                 
    rp5x = p5[0] * cos(ra) - p5[1] * sin(ra)
    rp5y = p5[0] * sin(ra) + p5[1] * cos(ra)                        
    rp6x = p6[0] * cos(ra) - p6[1] * sin(ra)                         
    rp6y = p6[0] * sin(ra) + p6[1] * cos(ra)
    rp1 = ( rp1x, rp1y )
    rp2 = ( rp2x, rp2y )
    rp3 = ( rp3x, rp3y )
    rp4 = ( rp4x, rp4y )
    rp5 = ( rp5x, rp5y )
    rp6 = ( rp6x, rp6y )

    sp1 = [rp1[0] * scale, rp1[1] * scale]
    sp2 = [rp2[0] * scale, rp2[1] * scale]
    sp3 = [rp3[0] * scale, rp3[1] * scale]
    sp4 = [rp4[0] * scale, rp4[1] * scale]
    sp5 = [rp5[0] * scale, rp5[1] * scale]
    sp6 = [rp6[0] * scale, rp6[1] * scale]

    return Hexagon(sp1, sp2, sp3, sp4, sp5, sp6)

def offsetHexagon(Hex, offsetx, offsety):
    Hex.p1[0] += offsetx;  Hex.p1[1] += offsety
    Hex.p2[0] += offsetx;  Hex.p2[1] += offsety
    Hex.p3[0] += offsetx;  Hex.p3[1] += offsety
    Hex.p4[0] += offsetx;  Hex.p4[1] += offsety
    Hex.p5[0] += offsetx;  Hex.p5[1] += offsety
    Hex.p6[0] += offsetx;  Hex.p6[1] += offsety
