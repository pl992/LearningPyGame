from init import *
import pygame

class character:
    def __init__(self,x,y,size):
        self.rect = pygame.Rect((x,y),(size,size))
        self.image = pygame.Surface((size,size))
        self.obscure = pygame.Surface((size,size))
        self.size = size
        self.obscure.fill((0,0,0))
        self.image.fill((255,255,255))
        #Horizontal,vertical
        self.velocity = [0,0]

        #left,right
        self.moving = [False,False]
        self.falling = True
        self.jump = False

    def fall(self,dt):
        if self.falling == True:
            self.velocity[1] += GRAVITY * dt

        if self.jump == True:
            self.jump = False
            self.velocity[1] -= JUMP 

    def move(self,dt):
        self.fall(dt)

    def update(self,screen_size,dt):
        self.move(dt)
        self.rect.move_ip(*self.velocity)

        if self.rect.left + self.velocity[0] > screen_size[0]:
            self.rect.left = self.velocity[0]
        elif self.rect.right + self.velocity[0] < 0:
            self.rect.right = screen_size[0] + self.velocity[0]
        elif self.rect.bottom + self.velocity[1] >= screen_size[1]:
            self.rect.bottom = screen_size[1]
            self.velocity[1] = 0
            self.falling = False
        elif self.rect.top + self.velocity[1] < 0:
            self.rect.top = 0
            self.velocity[1] = 0
