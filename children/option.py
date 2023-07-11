import enum

import pygame

from children.text import TEXT_STATIC_MODE, Text
from gameengine.basechild import BaseChild
from gameengine.mouse import Mouse
from gameengine.resources import Resources

CENTERED_DRAWING_MODE = enum.auto()


class OptionAttr:
    def __init__(self, idle, selected):
        self.idle_color = idle
        self.selected_color = selected


class Option(BaseChild):
    def __init__(
        self,
        rect,
        text,
        text_fg=(0, 0, 0),
        text_bg=None,
        attr=OptionAttr((150, 150, 150), (100, 100, 100)),
        mode=CENTERED_DRAWING_MODE,
    ):
        super().__init__()
        self.surface = pygame.Surface(rect.size)
        self.rect = pygame.FRect(rect)

        self.attr = attr

        self.w_text = Text(
            TEXT_STATIC_MODE,
            Resources.Fonts.get_from_file_buffer("MonoFonto", rect.h - 2),
            text_fg,
            text_bg,
            text,
        )
        self.add_children(self.w_text)
        self.set_mode(mode)

    def update(self):
        super().update()

        if self.rect.collidepoint(Mouse.pos):
            self.bg = self.attr.selected_color
        else:
            self.bg = self.attr.idle_color

    def set_mode(self, mode):
        if mode == CENTERED_DRAWING_MODE:
            self.w_text.rect.center = pygame.Vector2(self.rect.size) / 2
