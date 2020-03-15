import pygame
import player 

FPS = 60

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
        self._display_surf.blit(self.player.image,self.player.rect)
        pygame.display.update()

    def on_execute(self):
        while (self._running):
            self.dt = self.clock.tick(FPS) / 1000
            self._display_surf.blit(self.player.obscure,self.player.rect)
            self.player.update(self._display_surf.get_size(),self.dt)
            self.render()
            for event in pygame.event.get():
                self.on_event(event)
        self.on_quit()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

