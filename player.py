from init import *
import pygame
import character


class player(character.character):
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

        self.fall(dt)
    
    def stop(self,key):
        if key == pygame.K_a:
            self.moving[0] = False
        if key == pygame.K_d:
            self.moving[1] = False
