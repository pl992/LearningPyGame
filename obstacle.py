import pygame

class positions:
    def __init__(self,player):
        self.left = player.rect.left
        self.right = player.rect.right
        self.top = player.rect.top
        self.bottom = player.rect.bottom
        self.next_left = player.rect.left + player.velocity[0]
        self.next_right = player.rect.right + player.velocity[0]
        self.next_bottom = player.rect.bottom + player.velocity[1]
        self.next_top = player.rect.top + player.velocity[1]

class obstacle:
    def __init__(self,x,y,size):
        self.rect = pygame.Rect((x,y),(size,size))
        self.image = pygame.Surface((size,size))
        self.obscure = pygame.Surface((size,size))
        self.size = size
        self.obscure.fill((0,0,0))
        self.image.fill((255,255,255))

    def check_collision(self,player):
        get_sign = lambda x : -1 if x < 0 else 1
        pos = positions(player)
        #Everything works only if it's on movement
        #velocity[0] passes through the obstacle

        #Stop right
        if (pos.right <= self.rect.left and
                pos.next_right > self.rect.left and (
                pos.bottom >= self.rect.top and 
                pos.top <= self.rect.bottom)): 
            player.rect.right = self.rect.left
            player.velocity[0] = 0
        #Stop left
        if (pos.left >= self.rect.right and
                pos.next_left < self.rect.right and (
                pos.bottom >= self.rect.top and 
                pos.top <= self.rect.bottom)): 
            player.rect.left = self.rect.right
            player.velocity[0] = 0
        #Stop top
        if (pos.top >= self.rect.bottom and
                pos.next_top < self.rect.bottom and (
                pos.left >= self.rect.left and 
                pos.right <= self.rect.right)): 
            player.rect.top = self.rect.bottom
            player.velocity[1] = 0
        #Stop bottom
        if (pos.bottom <= self.rect.top and
                pos.next_bottom > self.rect.top and (
                pos.left >= self.rect.left and 
                pos.right <= self.rect.right)): 
            player.rect.bottom = self.rect.top
            player.velocity[1] = 0
        
        
#        if (player.rect.left + player.velocity[0] <= self.rect.right and
#                player.rect.right):
#            player.rect.left = self.rect.right
#            player.velocity[0] = 0
#        if player.rect.right + player.velocity[0] >= self.rect.left:
#            player.rect.right = self.rect.left
#            player.velocity[0] = 0

