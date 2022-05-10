import pygame
from core.widget import Widget
from os.path import abspath

class Logo(Widget):
    def __init__(self):
        super().__init__()
        path = abspath("containers/menu/images/logo.png")
        self.surface = pygame.image.load(path).convert_alpha()
