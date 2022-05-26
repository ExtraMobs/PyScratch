import pygame


class Widget:
    def __init__(self, program):
        self.program = program
        self.surface = pygame.Surface((0, 0))
        self.position = pygame.Vector2()
        self.rect = pygame.Rect(self.position, self.surface.get_size())

    def is_drawable(self):
        return type(self.surface) is pygame.Surface

    def update_rect(self):
        self.rect.topleft = self.position.xy
        self.rect.size = self.surface.get_size()

    def collide_point(self, point):
        if self.is_drawable():
            self.update_rect()
        return self.rect.collidepoint(point)
            

    def get_rect(self):
        if self.is_drawable():
            rect = self.surface.get_rect()
            rect.topleft = self.position
            return rect
        else:
            return pygame.Rect()

    def process_events(self, events): ...
    def process(self): ...
