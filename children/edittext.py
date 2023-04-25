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
        self.text_buffer = list(text)
        self.text = text

        self.fg_color = fg_color
        self.bg_color = bg_color

        self.expansion = expansion

        self.__offset = (math.floor(expansion), math.floor(expansion))

        self.surface = Resources.Surface.new(
            (size[0] + 2 * expansion, size[1] + 2 * expansion)
        )
        self.rect = pygame.FRect(self.surface.get_rect())

        self.need_draw = False

        self.draw_text()

    def draw_text(self):
        self.surface.fill(self.bg_color)
        self.font.render_to(
            self.surface,
            self.__offset,
            self.text,
            self.fg_color,
            self.bg_color,
        )

    def update_focus(self):
        super().update()

        for key_event in Keyboard.pressed_in_frame[pygame.KEYDOWN]:
            if key_event.key == pygame.K_BACKSPACE:
                del self.text_buffer[-1]
                self.need_draw = True
            elif (char := key_event.unicode).isprintable():
                self.text_buffer.append(char)
                self.need_draw = True
        if self.need_draw:
            self.text = "".join(self.text_buffer)
            self.draw_text()
