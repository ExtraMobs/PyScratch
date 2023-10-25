import enum

import pygame

from gameengine import resources
from gameengine.nodes.graphicnode import GraphicNode


class LateralBarButton(GraphicNode):
    def __init__(self, image):
        super().__init__(image)

    def update(self):
        self.rect.x = self.parent.rect.right
        self.rect.centery = self.parent.rect.centery

        mouse_device = self.program.devices.mouse
        if self.rect.collidepoint(mouse_device.pos):
            if mouse_device.get_pressed_down_in_frame(pygame.BUTTON_LEFT):
                self.parent.start_movement()

        super().update()

    def draw(self, _=None):
        super().draw(self.parent.parent.surface)


class LateralBar(GraphicNode):
    RIGHT = enum.auto()
    LEFT = enum.auto()

    default_speed = 1000
    speed = 0
    opened = False

    def __init__(self, size, button):
        super().__init__(resources.surface.new(size))
        self.orientation = self.LEFT

        self.add_children(button)

    def __check_off_the_lateral(self):
        if self.orientation == self.LEFT:
            return self.rect.x >= 0
        elif self.orientation == self.RIGHT:
            return self.rect.right <= self.parent.rect.width

    def __check_off_the_screen(self):
        if self.orientation == self.LEFT:
            return self.rect.right <= 0
        elif self.orientation == self.RIGHT:
            return self.rect.x >= self.parent.rect.width

    def update(self):
        if self.in_movement:
            self.rect.x += self.speed * self.program.time.delta
            if (self.opened and self.__check_off_the_screen()) or (
                not self.opened and self.__check_off_the_lateral()
            ):
                self.stop_movement()
        if not self.in_movement:
            if self.orientation == self.LEFT:
                if self.opened:
                    self.rect.x = 0
                else:
                    self.rect.x = -self.rect.width
            elif self.orientation == self.RIGHT:
                if self.opened:
                    self.rect.x = self.program.display.width
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
