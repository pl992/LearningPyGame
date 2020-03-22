import pygame

GRAVITY = 30
MAX_V = 10
ACC = 10
JUMP = 10

class player:
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

    def get_move(self,key):
        if key == pygame.K_a:
            self.moving[0] = True
            self.moving[1] = False
        if key == pygame.K_d:
            self.moving[0] = False
            self.moving[1] = True
        if key == pygame.K_w:
            self.falling = True
            self.jump = True

    def move(self,dt):
        get_sign = lambda x: -1 if x<0 else 1
        if self.moving[0] == True:
            if self.velocity[0] > -MAX_V:
                self.velocity[0] -= ACC * dt
            else:
                self.velocity[0] = -MAX_V

        if self.moving[1] == True:
            if self.velocity[0] < MAX_V:
                self.velocity[0] += ACC * dt
            else:
                self.velocity[0] = MAX_V

        if self.moving[0] == False and self.moving[1] == False:
            if self.velocity[0] != 0:
                sign = get_sign(self.velocity[0])
                self.velocity[0] += -1 * sign * ACC * dt
                if get_sign(self.velocity[0]) != sign:
                    self.velocity[0] = 0

        if self.falling == True:
            self.velocity[1] += GRAVITY * dt

        if self.jump == True:
            self.jump = False
            self.velocity[1] -= JUMP 
    
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

    def stop(self,key):
        if key == pygame.K_a:
            self.moving[0] = False
        if key == pygame.K_d:
            self.moving[1] = False
