import pygame

from children.menubutton import MenuButton
from gameengine.basechild import BaseChild
from gameengine.mouse import Mouse
from gameengine.resources import Resources


class List(BaseChild):
    def __init__(
        self, size, fg_color=(0, 0, 0), bg_color=(255, 255, 255), expansion=7, items=()
    ):
        super().__init__()
        self.items = [
            MenuButton(item, (size[0], 20), fg_color, bg_color, expansion)
            for item in items
        ]

        self.fg_color = fg_color
        self.bg_color = bg_color

        self.surface = Resources.Surface.new(size)
        self.rect = pygame.FRect(self.surface.get_rect())
        
        self.offset_y = 0
        
        self.draw_list()

    def _check_items(self):
        need_draw_list = False
        for item in self.items:
            item.update()
            if item.draw_updated and not need_draw_list:
                need_draw_list = True
        if need_draw_list:
            self.draw_list()

    def update(self):
        self._check_items()
        
        self.offset_y += Mouse.wheel.y * 27
        
        if self.offset_y != 0:
            self.draw_list()

    def draw_list(self):
        self.surface.fill(self.bg_color)
        items_rect = pygame.Vector2(0, self.offset_y)
        for item in self.items:
            self.surface.blit(item.surface, items_rect)
            item.rect.y = items_rect.y
            items_rect.y += 20
