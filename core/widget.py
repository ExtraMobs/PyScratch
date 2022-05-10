import pygame


class Widget:
    def __init__(self):
        self.surface = None
        self.position = pygame.math.Vector2()

    def is_drawable(self):
        return type(self.surface) is pygame.Surface

    def get_rect(self):
        if self.is_drawable():
            rect = self.surface.get_rect()
            rect.topleft = self.position
            return rect
        else:
            return pygame.Rect()

    def process_events(self, events): ...
