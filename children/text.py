import enum

import pygame

from gameengine.basechild import BaseChild

TEXT_STATIC_MODE = enum.auto()


class Text(BaseChild):
    def __init__(self, mode, font: pygame.font.Font, fg, bg=None, text="") -> None:
        super().__init__()
        self.font = font
        self.mode = mode
        self.fg = fg
        self.bg = bg

        self.set_text(text)

    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.fg, self.bg)
        if self.rect is None:
            self.rect = self.surface.get_frect()
        else:
            self.rect.size = self.surface.get_size()
