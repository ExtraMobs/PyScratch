from os.path import abspath

import pygame
from core.widget import Widget


class Logo(Widget):
    def __init__(self, program):
        super().__init__(program)
        path = abspath("containers/menu/images/logo.png")
        self.surface = pygame.image.load(path).convert_alpha()
