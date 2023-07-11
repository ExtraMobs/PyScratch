import enum

import pygame

from children.text import TEXT_STATIC_MODE, Text
from gameengine.basechild import BaseChild
from gameengine.resources import Resources

CENTERED_DRAWING_MODE = enum.auto()


class Option(BaseChild):
    def __init__(
        self,
        rect,
        bg,
        text,
        text_fg=(0, 0, 0),
        text_bg=None,
        mode=CENTERED_DRAWING_MODE,
    ):
        super().__init__()
        self.surface = pygame.Surface(rect.size)
        self.rect = pygame.FRect(rect)
        self.bg = bg

        self.w_text = Text(
            TEXT_STATIC_MODE,
            Resources.Fonts.get_from_file_buffer("MonoFonto", rect.h - 2),
            text_fg,
            text_bg,
            text,
        )
        self.add_children(self.w_text)
        self.set_mode(mode)

    def set_mode(self, mode):
        if mode == CENTERED_DRAWING_MODE:
            self.w_text.rect.center = pygame.Vector2(self.rect.size) / 2
