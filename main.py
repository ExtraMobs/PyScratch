import pygame
from managers import EventManager, FramerateManager, WindowManager
from objetcs import GraphicObject
from program import Program


class PyScratch(Program):
    def __init__(self):
        super().__init__(
            WindowManager(pygame.Window(self.__class__.__name__, (720, 405))),
            EventManager(),
            FramerateManager(60),
        )

        self.shape = Shape(self)

        self.run_loop()


class Shape(GraphicObject):
    def __init__(self, program):
        super().__init__(program)
        self.surface = pygame.Surface((50, 50))
        pygame.draw.polygon(
            self.surface, (255, 255, 255), [(0, 0), (10, 27), (50, 0), (41, 13)]
        )

    def process(self):
        print("test")

    def draw(self):
        self.display_surface.blit(self.surface, (0, 0))


PyScratch()
