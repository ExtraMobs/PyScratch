import pygame

from children.menubutton import MenuButton
from gameengine.basechild import BaseChild
from gameengine.engine import Engine
from gameengine.mouse import Mouse
from gameengine.resources import Resources


class List(BaseChild):
    __offset_mouse_y = 0

    moving_bar = False
    offset_y = 0

    def __init__(
        self,
        size,
        fg_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        expansion=7,
        button_size=20,
        items=(),
    ):
        super().__init__()

        self.surface = Resources.Surface.new(size)
        self.rect = pygame.FRect(self.surface.get_rect())

        self.bar_rect = pygame.Rect(0, 0, button_size, 0)
        self.items = [
            MenuButton(
                item,
                (self.rect.width - self.bar_rect.width - 2 * expansion, button_size),
                fg_color,
                bg_color,
                expansion,
            )
            for item in items
        ]
        self.button_size = button_size

        self.fg_color = fg_color
        self.bg_color = bg_color

        self.draw_list()

    def _check_items(self):
        self.__need_draw_list = False
        for item in self.items:
            item.update()
            if item.draw_updated and not self.__need_draw_list:
                self.__need_draw_list = True

    def _check_bar(self):
        self.bar_rect.x += self.rect.x
        self.bar_rect.y += self.rect.y
        if Mouse.get_pressed(pygame.BUTTON_LEFT):
            if self.moving_bar:
                items_height = len(self.items) * self.button_size
                relative_mouse_pos = Mouse.pos.y - self.__offset_mouse_y
                mouse_ratio = relative_mouse_pos / self.rect.height
                self.offset_y = -(mouse_ratio * items_height)
            elif Mouse.pos.x > self.bar_rect.x:
                if self.bar_rect.collidepoint(Mouse.pos):
                    self.moving_bar = True
                    self.__offset_mouse_y = Mouse.pos.y - self.bar_rect.y
                else:
                    add_offset_y = self.button_size * 500 * Engine.deltatime
                    if Mouse.pos.y > self.bar_rect.y:
                        add_offset_y = -add_offset_y
                    self.offset_y += add_offset_y
        else:
            self.moving_bar = False
        self.bar_rect.x -= self.rect.x
        self.bar_rect.y -= self.rect.y

    def update(self):
        super().update()
        if self.rect.collidepoint(Mouse.pos):
            self._check_bar()
        self._check_items()

        if not self.moving_bar:
            self.offset_y += Mouse.wheel.y * self.button_size * 5

        if self.offset_y != 0 or self.__need_draw_list:
            self.draw_list()

    def draw_list(self):
        self.surface.fill(self.bg_color)

        if self.offset_y < (
            bottom := (len(self.items) * self.button_size - self.rect.height) * -1
        ):
            self.offset_y = bottom
        elif self.offset_y > 0:
            self.offset_y = 0

        items_rect = pygame.Vector2(0, self.offset_y)
        for item in self.items:
            self.surface.blit(item.surface, items_rect)
            item.rect.y = items_rect.y
            items_rect.y += self.button_size + 2 * item.expasion

        pygame.draw.rect(
            self.surface,
            (127, 127, 127),
            pygame.Rect(
                self.rect.right - self.bar_rect.width,
                0,
                self.bar_rect.width,
                self.rect.height,
            ),
        )

        height = len(self.items) * self.button_size
        self.bar_rect.height = self.rect.height / height * self.rect.height
        if height > self.rect.height:
            self.bar_rect.y = (
                self.offset_y / bottom * (self.rect.height - self.bar_rect.height)
            )
            self.bar_rect.right = self.rect.right
            pygame.draw.rect(self.surface, (0, 0, 0), self.bar_rect)
