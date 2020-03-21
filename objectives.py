import pygame
import numpy as np

class objective:
    def __init__(self,x,y,size):
        self.pos = (x,y)
        self.image = pygame.Surface((size,size))
        self.center = (size//2,size//2)
        self.radius = size//2
        pygame.draw.circle(self.image,(0,255,0),self.center,self.radius)
        self.obscure = pygame.Surface((size,size))
        self.size = size
        self.obscure.fill((0,0,0))

        self.left = self.pos[0] - self.radius
        self.right = self.pos[0] + self.radius
        self.top = self.pos[1] - self.radius
        self.bottom = self.pos[1] + self.radius
    
    def got_it(self,player):
        corners = [
                    [player.rect.left,player.rect.top],
                    [player.rect.right,player.rect.top],
                    [player.rect.left,player.rect.bottom],
                    [player.rect.right,player.rect.bottom]
                  ]
        got = False
                   
               
        for i in corners:
            position = np.square(i[0] - (self.pos[0] + self.radius)) + np.square(i[1] - (self.pos[1] + self.radius))
            if position < np.square(self.radius):
                got = True

        if self.size < player.size:
            if player.rect.top <= self.top and player.rect.bottom > self.bottom:
                if (
                        (player.rect.left > self.left and player.rect.right < self.left) or 
                        (player.rect.right > self.right and player.rect.left < self.left)
                    ):
                    got = True
            if player.rect.left <= self.left and player.rect.right > self.right:
                if (
                        (player.rect.bottom > self.bottom and player.rect.top < self.top) or 
                        (player.rect.top > self.top and player.rect.bottom < self.bottom)
                    ):
                    got = True

        if got == True:
            self.image = self.obscure

        return got
