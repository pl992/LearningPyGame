import pygame
import random
import obstacle
import player 
import objectives

FPS = 60
random.seed(10)

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640,400
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size,pygame.HWSURFACE)
        self.background = pygame.Surface(self._display_surf.get_size())
        self.background.fill((0,0,0))
        self.objectives = []
        self.obstacles = []

        pygame.init()
        self.player = player.player(10,10,20)
        self.winning_pics = [pygame.image.load('YouWinMovie/{0:03d}.png'.format(i)) for i in range(1,5)]

    def start_level(self,filename):
        with open(filename,'r') as f:
            target = 'obs'
            for i in f.readlines():
                line = i.split()
                if line[0] == '*':
                    target = 'obj'
                else:
                    if target == 'obs':
                        self.obstacles.append(obstacle.obstacle(
                                              float(line[0]),
                                              float(line[1]),
                                              (int(line[2]),int(line[3]))))
                    elif target == 'obj':
                        self.objectives.append(objectives.objective(
                                              float(line[0]),
                                              float(line[1]),
                                              int(line[2])))
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
        for i in self.obstacles:
            self._display_surf.blit(i.image,i.rect)
        self._display_surf.blit(self.player.image,self.player.rect)
        pygame.display.update()

    def on_execute(self):
        n_im = 0
        starting = True
        while (self._running):
            if starting:
                self.start_level('levels/1.dat')
                starting = False

            if self.score <= len(self.objectives):
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
                # This has to be done after the render because the 
                # spot has to be cleaned
                if not objective_del == -1:
                    del self.objectives[objective_del]
            else:
                if n_im > len(self.winning_pics) - 1:
                    n_im = 0
                self._display_surf.blit(self.winning_pics[n_im],(0,0))
                pygame.display.update()
                pygame.time.wait(50)
                n_im+=1

            for event in pygame.event.get():
                self.on_event(event)
        self.on_quit()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

