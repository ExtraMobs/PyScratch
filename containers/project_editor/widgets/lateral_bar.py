import pygame
from core.widget import Widget


class LateralBar(Widget):
    def __init__(self, program):
        super().__init__(program)
        self.surface = pygame.Surface((300, 720))