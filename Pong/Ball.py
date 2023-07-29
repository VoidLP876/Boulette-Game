from math import sin, cos, pow, sqrt, radians, pi
import pygame
pygame.init()
effect =pygame.mixer.Sound('Assets/boing.mp3')
class Ball:
    def __init__(self, X, Y, speed):#sprite):
        self.r = 0
        self.x = X
        self.y = Y
        self.speed = speed
        self.Vx = 0
        self.Vy = speed
        self.sprite = pygame.image.load("Assets/boulettev3.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
    def Draw(self, window):
        # pygame.draw.circle(screen, "white", (self.x, self.y), 5)
        window.blit(self.sprite, (self.x - 25, self.y - 25))
    def MoveBall(self, dt):
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        if self.x < 340:
            self.Vx *= -1
            self.x += self.Vx * dt
            return 1
        if self.x > 1060:
            self.Vx *= -1
            self.x += self.Vx * dt
            return 3
        if self.y < 0:
            self.Vy *= -1
            self.y += self.Vy * dt
            return 0
        if self.y > 720:
            self.Vy *= -1
            self.y += self.Vy * dt
            return 2
        return -1

    def RetargetX(self, player, isInverted, rotation):
        offset = self.y - (player.y + player.height / 2)
        t = offset / (player.height / 2)
        if rotation:
            t *= -1
        angle = pi / 4 * t
        self.Vx = self.speed * cos(angle) * isInverted
        self.Vy = self.speed * sin(angle) * isInverted

    def RetargetY(self, player, isInverted, rotation):
        offset = self.x - (player.x + player.width / 2)
        t = offset / (player.width / 2)
        if rotation:
            t *= -1
        angle = pi / 4 * t
        self.Vx = self.speed * sin(angle) * isInverted
        self.Vy = self.speed * cos(angle) * isInverted
        
    def CollidePaddles(self, paddles):
        returnTrue = False
        for i, paddle in enumerate(paddles):
            if paddle.x < self.x and self.x <= paddle.x + paddle.width and paddle.y < self.y and self.y <= paddle.y + paddle.height:
                effect.play()
                
                returnTrue = True
                match i:
                    case 0:
                        self.RetargetY(paddle,  1, 0)
                    case 1:
                        self.RetargetX(paddle,  1, 0)
                    case 2:
                        self.RetargetY(paddle, -1, 1)
                    case 3:
                        self.RetargetX(paddle, -1, 1)
        
        return returnTrue