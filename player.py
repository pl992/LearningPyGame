import pygame

class player:
    def __init__(self,x,y,size):
        self.rect = pygame.Rect((x,y),(size,size))
        self.image = pygame.Surface((size,size))
        self.obscure = pygame.Surface((size,size))
        self.size = size
        self.obscure.fill((0,0,0))
        self.image.fill((255,255,255))
        self.velocity = [0,0]

    def get_move(self,key,dt):
        if key == pygame.K_w:
            self.velocity[1] = -200 * dt
        if key == pygame.K_s:
            self.velocity[1] = 200 * dt
        if key == pygame.K_a:
            self.velocity[0] = -200 * dt
        if key == pygame.K_d:
            self.velocity[0] = 200 * dt

    def update(self,screen_size):
        if self.rect.left + self.velocity[0] > screen_size[0]:
            self.rect.left = self.velocity[0]
        elif self.rect.right + self.velocity[0] < 0:
            self.rect.right = screen_size[0] + self.velocity[0]
        elif self.rect.top + self.velocity[1] > screen_size[1]:
            self.rect.top = self.velocity[1]
        elif self.rect.bottom + self.velocity[1] < 0:
            self.rect.bottom = screen_size[1] + self.velocity[1]
        else:
            self.rect.move_ip(*self.velocity)

    def stop(self,key):
        if key == pygame.K_w or key == pygame.K_s:
            self.velocity[1] = 0
        elif key == pygame.K_a or key == pygame.K_d:
            self.velocity[0] = 0

