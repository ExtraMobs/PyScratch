import pygame
from core.container import Container
from containers.project_editor.widgets.lateral_bar import LateralBar

class ProjectEditor(Container):
    def __init__(self, program):
        super().__init__(program)
        self.lateral_bar = LateralBar(program)
        self.add_widgets(self.lateral_bar)
        
    def process_events(self, events):
        super().process_events(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.program.stop()
