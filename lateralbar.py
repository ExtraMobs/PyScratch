import enum

import pygame

from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode


class LateralBarButton(GraphicNode):
    def __init__(self, image):
        super().__init__(image)

    def update(self):
        self.rect.left = self.parent.rect.right
        self.rect.centery = self.parent.rect.centery

        mouse_device = self.program.devices.mouse
        if self.rect.collidepoint(mouse_device.pos):
            if mouse_device.get_pressed_down_in_frame(pygame.BUTTON_LEFT):
                self.parent.start_movement()

        super().update()

    def draw(self, _=None):
        super().draw(self.parent.parent.surface)


class RectChecker:
    lateral_bar = None

    def __init__(self, lateral_bar):
        self.lateral_bar = lateral_bar

    @property
    def is_inside_screen(self):
        if self.lateral_bar.orientation == self.lateral_bar.LEFT:
            return self.lateral_bar.rect.left >= 0
        elif self.orientation == self.lateral_bar.RIGHT:
            return self.lateral_bar.rect.right <= self.lateral_bar.parent.rect.right

    @property
    def is_off_screen(self):
        if self.lateral_bar.orientation == self.lateral_bar.LEFT:
            return self.lateral_bar.rect.right <= 0
        elif self.lateral_bar.orientation == self.RIGHT:
            return self.rect.left >= self.parent.rect.right


class LateralBar(GraphicNode):
    RIGHT = enum.auto()
    LEFT = enum.auto()

    default_speed = 1000
    speed = 0
    opened = False
    orientation = None

    rect_checker = None

    def __init__(self, size, button):
        super().__init__(resources.surface.new(size))
        self.orientation = self.LEFT

        self.add_children(button)

        self.rect_checker = RectChecker(self)

    def update(self):
        if self.in_movement:
            self.rect.left += self.speed * self.program.time.delta
            if (self.opened and self.rect_checker.is_off_screen) or (
                not self.opened and self.rect_checker.is_inside_screen
            ):
                self.stop_movement()

        if not self.in_movement:
            if self.orientation == self.LEFT:
                if self.opened:
                    self.rect.left = 0
                else:
                    self.rect.left = -self.rect.width
            elif self.orientation == self.RIGHT:
                if self.opened:
                    self.rect.left = self.program.display.width
                else:
                    self.rect.right = self.parent.rect.width
        super().update()

    def start_movement(self):
        self.in_movement = True

    def stop_movement(self):
        self.in_movement = False
        self.opened = not self.opened

    @property
    def in_movement(self):
        return self.speed != 0

    @in_movement.setter
    def in_movement(self, value):
        if value:
            if self.orientation == self.LEFT:
                self.speed = self.default_speed
            elif self.orientation == self.RIGHT:
                self.speed = -self.default_speed
            if self.opened:
                self.speed *= -1
        else:
            self.speed = 0
