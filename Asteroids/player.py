import pygame
from math import sin, cos, radians

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
v = pygame.Vector2(1,1)  

def clamp(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n
    
def makeTriangle(scale, internalAngle, rotation):
    #define the points in a uint space
    ia = (radians(internalAngle) * 2) - 1
    p1 = (0, 1)
    p2 = (cos(ia), sin(ia))
    p3 = (cos(ia) * -1, sin(ia))

    #rotate the points
    ra = radians(rotation)
    rp1x = p1[0] * cos(ra) - p1[1] * sin(ra)
    rp1y = p1[0] * sin(ra) + p1[1] * cos(ra)                 
    rp2x = p2[0] * cos(ra) - p2[1] * sin(ra)
    rp2y = p2[0] * sin(ra) + p2[1] * cos(ra)                        
    rp3x = p3[0] * cos(ra) - p3[1] * sin(ra)                         
    rp3y = p3[0] * sin(ra) + p3[1] * cos(ra)
    rp1 = ( rp1x, rp1y )
    rp2 = ( rp2x, rp2y )
    rp3 = ( rp3x, rp3y )

    #scale the points 
    sp1 = [rp1[0] * scale, rp1[1] * scale]
    sp2 = [rp2[0] * scale, rp2[1] * scale]
    sp3 = [rp3[0] * scale, rp3[1] * scale]
                    
    return Triangle(sp1, sp2, sp3)

def drawTriangle(tri, screen,color=(255, 255, 255)):
    pygame.draw.line(screen, color, tri.p1, tri.p2)
    pygame.draw.line(screen, color, tri.p2, tri.p3)
    pygame.draw.line(screen, color, tri.p3, tri.p1)

def offsetTriangle(triangle, offsetx, offsety):
    triangle.p1[0] += offsetx;  triangle.p1[1] += offsety;
    triangle.p2[0] += offsetx;  triangle.p2[1] += offsety;
    triangle.p3[0] += offsetx;  triangle.p3[1] += offsety;

class Player:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.Vx = 0
        self.Vy = 0
        self.Score = 0
        self.Life = 1
    def Input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.Vy-= 2
        if keys[pygame.K_s]:
            self.Vy +=2
        if keys[pygame.K_q]:
            self.Vx-= 2
        if keys[pygame.K_d]:
            self.Vx += 2
        self.Vx /= 1.08
        self.Vy /= 1.08
            
    def PlayerMovement(self, screen):
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy
        self.x = clamp(self.x, 0, screen.get_width())
        self.y = clamp(self.y, 0, screen.get_height())