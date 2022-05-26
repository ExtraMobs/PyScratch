import pygame
from containers.menu.widgets.button_new_project import ButtonNewProject
from containers.menu.widgets.button_load_project import ButtonLoadProject
from containers.menu.widgets.logo import Logo
from core.container import Container


class Menu(Container):
    def __init__(self, program):
        super().__init__(program)
        self.logo = Logo(program)
        self.b_newproject = ButtonNewProject(program)
        self.b_loadproject = ButtonLoadProject(program)
        self.add_widgets(self.logo, self.b_newproject, self.b_loadproject)

        self.logo.position.x = self.program.window.get_rect().centerx - self.logo.get_rect().centerx

        self.b_newproject.position.x = self.program.window.get_rect().centerx - self.b_newproject.get_rect().centerx
        self.b_newproject.position.y = 300
        
        self.b_loadproject.position.x = self.program.window.get_rect().centerx - self.b_loadproject.get_rect().centerx
        self.b_loadproject.position.y = 400

    def process_events(self, events):
        super().process_events(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.program.stop()
