import pygame
from containers.menu.widgets.logo import Logo
from core.container import Container

class Menu(Container):
    def __init__(self, program):
        super().__init__(program)
        self.logo = Logo()
        self.add_widgets(self.logo)
        
        self.logo.position.x = self.program.window.get_rect().centerx - self.logo.get_rect().centerx
        print(self.logo.position)

    def process_events(self, events):
        super().process_events(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.program.stop()
