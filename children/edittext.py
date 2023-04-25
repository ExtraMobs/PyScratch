import math
from os import path

import pygame
import pygame.freetype

from gameengine.basechild import BaseChild
from gameengine.keyboard import Keyboard
from gameengine.mouse import Mouse
from gameengine.resources import Resources


class EditText(BaseChild):
    def __init__(
        self, size, text="", fg_color=(0, 0, 0), bg_color=(255, 255, 255), expansion=7
    ):
        super().__init__()
        self.font = pygame.freetype.Font(path.abspath("monofonto rg.otf"), 20)
        self.text = text

        self.fg_color = fg_color
        self.bg_color = bg_color

        self.expansion = expansion

        self.__offset = (math.floor(expansion), math.floor(expansion))

        self.surface = Resources.Surface.new(
            (size[0] + 2 * expansion, size[1] + 2 * expansion)
        )
        self.rect = pygame.FRect(self.surface.get_rect())

        self.draw_text()

    def draw_text(self):
        self.surface.fill(self.bg_color)
        self.font.render_to(
            self.surface, self.__offset, self.text, self.fg_color, self.bg_color
        )

    def update(self):
        super().update()

        if self.rect.collidepoint(Mouse.pos):
            for key_event in Keyboard.pressed_in_frame:
                # if key_event.
                pass
