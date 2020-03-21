import pygame
import random
import obstacle
import player 
import objectives

FPS = 60
N_OBJECTIVES = 5

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640,400
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size,pygame.HWSURFACE)
        self.background = pygame.Surface(self._display_surf.get_size())
        self.background.fill((0,0,0))

        pygame.init()
        self.player = player.player(10,10,20)
        self.objectives = [objectives.objective(random.randint(0,self.weight),random.randint(0,self.height),random.randint(10,50)) for i in range(N_OBJECTIVES)]
        self.objectives.append(objectives.objective(100,self.height-15,10))
        self.obstacles = [obstacle.obstacle(random.randint(0,self.weight),random.randint(0,self.height),random.randint(10,50)) for i in range(5)]
        self.score = 0
        self.render()

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            self.player.get_move(event.key)
        elif event.type == pygame.KEYUP:
            self.player.stop(event.key)

    def on_quit(self):
        pygame.quit()

    def render(self):
        for i in self.objectives:
            self._display_surf.blit(i.image,i.pos)
        self._display_surf.blit(self.player.image,self.player.rect)
        for i in self.obstacles:
            self._display_surf.blit(i.image,i.rect)
        pygame.display.update()

    def on_execute(self):
        while (self._running) and (self.score <= N_OBJECTIVES):
            self.dt = self.clock.tick(FPS) / 1000
            self._display_surf.blit(self.player.obscure,self.player.rect)
            self.player.update(self._display_surf.get_size(),self.dt)
            

            objective_del = -1
            for i,obj in enumerate(self.objectives):
                if obj.got_it(self.player):
                    self.score += 1
                    objective_del = i


            for i in self.obstacles:
                i.check_collision(self.player)
            self.render()
            if not objective_del == -1:
                del self.objectives[objective_del]
            for event in pygame.event.get():
                self.on_event(event)
        self.on_quit()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

