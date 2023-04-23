import math
from os import path

import pygame
import pygame.freetype

from gameengine.basechild import BaseChild
from gameengine.mouse import Mouse
from gameengine.resources import Resources


class MenuButton(BaseChild):
    __last_size = (0, 0)
    draw_updated = False

    def __init__(
        self, text, size=None, fg_color=(0, 0, 0), bg_color=(255, 255, 255), expansion=7
    ):
        super().__init__()
        self.font = pygame.freetype.Font(path.abspath("monofonto rg.otf"), 20)
        self.text = text

        self.fg_color = fg_color
        self.bg_color = bg_color

        self.expasion = expansion

        self.__offset = (math.floor(expansion), math.floor(expansion))

        text_rect = self.font.get_rect(text)
        text_rect.topleft = self.__offset

        if size is None:
            self.fixed_size = False
            size = (text_rect.right + expansion, text_rect.bottom + expansion)
        else:
            self.fixed_size = True
        self.surface = Resources.Surface.new(size)
        self.rect = pygame.FRect(self.surface.get_rect())

        self.__last_size = size

        self.draw_text()

    def draw_text(self):
        if not self.fixed_size:
            rect = self.font.get_rect(self.text)
            if rect.size != self.__last_size:
                self.__last_size = rect.size

                rect.topleft = self.__offset
                self.surface = Resources.Surface.new(
                    (rect.right + self.expasion, rect.bottom + self.expasion)
                )
        self.surface.fill(self.bg_color)
        self.font.render_to(
            self.surface,
            self.__offset,
            self.text,
            self.fg_color,
            self.bg_color,
        )
        self.draw_updated = True

    def _check_mouse_collision(self):
        def check_color(color):
            if self.bg_color != color:
                self.bg_color = color
                self.draw_text()

        self.draw_updated = False
        
        if self.rect.collidepoint(Mouse.pos):
            check_color((127, 127, 127))
        else:
            check_color((255, 255, 255))

    def update(self):
        super().update()
        self._check_mouse_collision()
