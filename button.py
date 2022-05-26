import pygame

from core.widget import Widget


class Button(Widget):
    def __init__(self, program, surface, surface_selected):
        super().__init__(program)
        self.surface = surface
        self.default_surface = surface
        self.surface_selected = surface_selected
        
    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
                if self.collide_point(pos):
                    self.surface = self.surface_selected
                else:
                    self.surface = self.default_surface
