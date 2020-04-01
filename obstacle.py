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
        self.rect = pygame.Rect((x,y),size)
        self.image = pygame.Surface(size)
        self.obscure = pygame.Surface(size)
        self.size = size
        self.obscure.fill((0,0,0))
        self.image.fill((255,0,0))

    def check_collision(self,player):
        get_sign = lambda x : -1 if x < 0 else 1
        pos = positions(player)

        #Stop right
        if (pos.right <= self.rect.left and
                pos.next_right > self.rect.left):
            if (
                    (
                        pos.bottom >= self.rect.top and 
                        pos.top <= self.rect.bottom
                    ) or
                    (
                        pos.bottom >= self.rect.bottom and
                        pos.top <= self.rect.top
                    )
                ): 
                player.rect.right = self.rect.left
                player.velocity[0] = 0
        #Stop left
        if (pos.left >= self.rect.right and
                pos.next_left < self.rect.right):
            if (
                    (
                        pos.bottom >= self.rect.top and 
                        pos.top <= self.rect.bottom 
                    ) or
                    (
                        pos.bottom >= self.rect.bottom and
                        pos.top <= self.rect.top
                    )
                ):
                player.rect.left = self.rect.right
                player.velocity[0] = 0
        #Stop top
        if (
                pos.top < self.rect.bottom and
                pos.bottom > self.rect.bottom):
            if (
                    (
                        pos.left > self.rect.left and 
                        pos.left < self.rect.right
                    ) or
                    (
                        pos.right > self.rect.left and
                        pos.right < self.rect.right
                    )or
                    (
                        pos.left <= self.rect.left and 
                        pos.right >= self.rect.right
                    )
                ):
                player.rect.top = self.rect.bottom
                player.velocity[1] = 0
        #Stop bottom 
        if (
                pos.bottom <= self.rect.top and
                pos.next_bottom > self.rect.top
            ):
            if (
                (
                    pos.left > self.rect.left and 
                    pos.left < self.rect.right) or 
                (
                    pos.right > self.rect.left and
                    pos.right < self.rect.right
                ) or
                (
                    pos.left <= self.rect.left and 
                    pos.right >= self.rect.right
                )
                ):
                player.rect.bottom = self.rect.top
                player.velocity[1] = 0
